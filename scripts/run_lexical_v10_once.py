"""One real diagnostic/revision sequence per route, no retries or external judge."""
import argparse, concurrent.futures, hashlib, json, os, re, shutil, subprocess, tempfile, time
from pathlib import Path
import urllib.request, urllib.error
from validate_lexical_v10 import validate_diagnosis, validate_revision

def save(p, x): p.write_text(json.dumps(x, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
def read(p): return json.loads(p.read_text(encoding='utf-8'))
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def call(route, folder, system, prompt):
    folder.mkdir(parents=True)
    (folder/'system.txt').write_text(system, encoding='utf-8')
    (folder/'prompt.txt').write_text(prompt, encoding='utf-8')
    meta={'route':route,'status':'failed','automatic_retries':0,'started':time.time()}
    text=''
    try:
        if route['provider']=='ollama':
            token=os.environ.get('OLLAMA_API_KEY','').strip()
            if not token: token=(Path.home()/'.codex/secrets/ollama-cloud-api-key.txt').read_text(encoding='utf-8-sig').strip()
            body={'model':route['model'],'instructions':system,'input':prompt,'stream':False,'temperature':0,'max_output_tokens':32768,'truncation':'disabled'}
            req=urllib.request.Request('https://ollama.com/v1/responses',data=json.dumps(body).encode(),headers={'Authorization':'Bearer '+token,'Content-Type':'application/json'})
            with urllib.request.urlopen(req,timeout=360) as response: raw=json.load(response)
            text='\n'.join(c['text'] for i in raw.get('output',[]) for c in i.get('content',[]) if c.get('type')=='output_text')
            meta.update(resolved_model=raw.get('model'),usage=raw.get('usage'),response_status=raw.get('status'))
        elif route['provider']=='claude':
            with tempfile.TemporaryDirectory(prefix='ko-v10-') as cwd:
                cmd=[shutil.which('claude'),'-p','--model',route['model'],'--setting-sources','','--system-prompt',system,'--tools','','--disable-slash-commands','--permission-mode','dontAsk','--no-session-persistence','--no-chrome','--strict-mcp-config','--mcp-config','{"mcpServers":{}}','--output-format','json']
                proc=subprocess.run(cmd,input=prompt,cwd=cwd,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=360)
            (folder/'stderr.txt').write_text(proc.stderr,encoding='utf-8')
            raw=json.loads(proc.stdout); text=raw.get('result','');meta.update(exit_code=proc.returncode,model_usage=raw.get('modelUsage'))
        else:
            with tempfile.TemporaryDirectory(prefix='ko-v10-') as cwd:
                cmd=[shutil.which('codex'),'exec','--ignore-user-config','--ephemeral','--skip-git-repo-check','-s','read-only','-m',route['model'],'-C',cwd,'--json','-o',str((folder/'answer.txt').resolve()),'-']
                proc=subprocess.run(cmd,input=system+'\n\n'+prompt,cwd=cwd,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=360)
            (folder/'events.jsonl').write_text(proc.stdout,encoding='utf-8')
            (folder/'stderr.txt').write_text(proc.stderr,encoding='utf-8')
            meta.update(exit_code=proc.returncode,delivery='user_prompt_in_codex_cli',resolved_model='not_independently_verified')
            if (folder/'answer.txt').exists(): text=(folder/'answer.txt').read_text(encoding='utf-8')
        (folder/'output.txt').write_text(text,encoding='utf-8')
        data=json.loads(re.sub(r'^```(?:json)?\s*|\s*```$','',text.strip()))
        save(folder/'parsed.json',data);meta['status']='returned_json'
    except urllib.error.HTTPError as e: meta['error']='http_'+str(e.code)
    except Exception as e: meta['error']=type(e).__name__
    meta.update(elapsed=round(time.time()-meta['started'],2),prompt_sha256=digest(folder/'prompt.txt'),system_sha256=digest(folder/'system.txt'))
    save(folder/'metadata.json',meta)
    return meta

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--prepared',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    exp=a.output.resolve();exp.mkdir(parents=True,exist_ok=False)
    inputs=read(a.prepared/'inputs.json')['revision']
    selected={'T001','T006','T021','T030','T033','T036','T041','T048',*[f'T{i:03d}' for i in range(51,57)]}
    cases=[x for x in inputs if x['id'] in selected]
    routes=read(a.prepared/'routes.json')['models']+[{'provider':'codex','model':m} for m in ['gpt-5.5','gpt-5.6-sol','gpt-5.6-terra']]
    prompts=read(Path(__file__).resolve().parents[1]/'evals/lexical-expression-v10/prompts.json')
    system=prompts['base']+'\n'+prompts['natural']+'\n'+(a.prepared/'skill-revised.txt').read_text(encoding='utf-8')+'\nDo not use tools, browse, or read files. Return only the requested JSON.'
    save(exp/'inputs.json',cases);save(exp/'plan.json',{'routes':routes,'repetitions':1,'arm':'NS','mode':'diagnostic_then_revision','cases':len(cases),'no_control_arm':True,'no_external_judge':True})
    save(exp/'prompts.json',prompts);(exp/'system.txt').write_text(system,encoding='utf-8')
    save(exp/'freeze.json',{'files':{p.name:digest(p) for p in exp.iterdir() if p.is_file()},'runner':digest(Path(__file__))})
    def worker(route):
        root=exp/route['model'].replace(':','-'); rows=[]
        prompt=prompts['diagnose']+'\n모든 대상에 대한 응답을 {"items": [...]}로 반환하세요.\n'+json.dumps(cases,ensure_ascii=False)
        meta=call(route,root/'diagnosis',system,prompt);rows.append(meta)
        if meta['status']=='returned_json':
            try:
                diagnosis=read(root/'diagnosis/parsed.json');items=diagnosis['items']
                assert len(items)==len(cases) and {x['case_id'] for x in items}==selected
                for c in cases:validate_diagnosis(c['target'],next(x for x in items if x['case_id']==c['id']),c['id'])
                save(root/'diagnosis/validated.json',{'valid':True,'sha256':digest(root/'diagnosis/parsed.json')})
                prompt=prompts['revise_after_diagnosis']+'\n모든 대상에 대한 응답을 {"items": [...]}로 반환하세요.\n원문:\n'+json.dumps(cases,ensure_ascii=False)+'\n고정 진단:\n'+json.dumps(diagnosis,ensure_ascii=False)
                result=call(route,root/'revision',system,prompt);rows.append(result)
                if result['status']=='returned_json':
                    revisions=read(root/'revision/parsed.json')['items']
                    assert len(revisions)==len(cases) and {x['case_id'] for x in revisions}==selected
                    for d in items:validate_revision(d,next(x for x in revisions if x['case_id']==d['case_id']))
                    save(root/'revision/validated.json',{'valid':True})
            except Exception as e:save(root/'validation-error.json',{'error':type(e).__name__,'revision_not_retried':True})
        print(json.dumps({'model':route['model'],'stages':[r['status'] for r in rows],'errors':[r.get('error') for r in rows]}),flush=True)
        return rows
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool: results=list(pool.map(worker,routes))
    save(exp/'summary.json',results)

if __name__=='__main__':main()
