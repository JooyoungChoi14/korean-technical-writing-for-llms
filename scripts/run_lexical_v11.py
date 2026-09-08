"""Single-case, one-repeat N/NS diagnostic then revision experiment."""
import argparse, concurrent.futures, hashlib, json, os, re, threading, time, urllib.request, urllib.error
from pathlib import Path
from run_lexical_v10_once import call as cli_call

def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s):return re.sub(r'\s+','',s)

def check_diagnosis(case,d):
    if not isinstance(d,dict) or d.get('case_id')!=case['id'] or d.get('decision') not in ['issue','none','uncertain'] or not isinstance(d.get('findings'),list):
        return {'usable':False,'error':'schema'}
    seen=set();locations=[]
    for f in d['findings']:
        if not isinstance(f,dict) or not isinstance(f.get('finding_id'),str) or f['finding_id'] in seen or not isinstance(f.get('quote'),str) or not f['quote'] or type(f.get('occurrence')) is not int or f['occurrence']<1 or not isinstance(f.get('reason'),str) or f.get('judgment') not in ['revise','keep','uncertain']:
            return {'usable':False,'error':'finding_schema'}
        if not norm(f['quote']):return {'usable':False,'error':'empty_quote'}
        seen.add(f['finding_id']);q=f['quote'];n=f['occurrence'];target=case['target'];context=case.get('context_before','')+'\n'+case.get('context_after','')
        location='exact' if target.count(q)>=n else ('whitespace_equivalent' if norm(target).count(norm(q))>=n else ('context_only' if norm(q) in norm(context) else 'not_in_source'))
        locations.append({'finding_id':f['finding_id'],'location':location})
    return {'usable':True,'locations':locations,'decision_inconsistent':d['decision']=='none' and bool(d['findings'])}

def check_revision(d,r):
    if not isinstance(r,dict) or r.get('case_id')!=d['case_id'] or not isinstance(r.get('text'),str) or not r['text'].strip() or not isinstance(r.get('actions'),list):return {'usable':False,'error':'schema'}
    errors=[];seen=[]
    for a in r['actions']:
        if not isinstance(a,dict):errors.append('action_schema');continue
        if not isinstance(a.get('finding_id'),str):errors.append('action_id_schema');continue
        seen.append(a.get('finding_id'));action=a.get('action');replacement=a.get('replacement')
        if action not in ['revise','keep','clarify'] or (action=='revise' and not isinstance(replacement,str)) or (action in ['keep','clarify'] and replacement is not None and not isinstance(replacement,str)):errors.append('action_schema')
    expected={f['finding_id'] for f in d['findings']}
    if set(seen)!=expected or len(seen)!=len(set(seen)):errors.append('finding_link')
    return {'usable':True,'action_errors':errors}

def invoke(route,folder,system,prompt):
    if route['provider']!='ollama':return cli_call(route,folder,system,prompt)
    folder.mkdir(parents=True,exist_ok=False);(folder/'prompt.txt').write_text(prompt,encoding='utf-8');(folder/'system.txt').write_text(system,encoding='utf-8')
    body={'model':route['model'],'instructions':system,'input':prompt,'stream':False,'temperature':0,'truncation':'disabled'}
    save(folder/'request.json',body);meta={'route':route,'status':'failed','output_limit':'omitted','automatic_retries':0};start=time.time()
    try:
        token=os.environ.get('OLLAMA_API_KEY','').strip()
        if not token:token=(Path.home()/'.codex/secrets/ollama-cloud-api-key.txt').read_text(encoding='utf-8-sig').strip()
        req=urllib.request.Request('https://ollama.com/v1/responses',data=json.dumps(body).encode(),headers={'Authorization':'Bearer '+token,'Content-Type':'application/json'})
        with urllib.request.urlopen(req,timeout=360) as response:raw=response.read()
        (folder/'response.raw.json').write_bytes(raw);data=json.loads(raw)
        text='\n'.join(c.get('text','') for i in data.get('output',[]) for c in i.get('content',[]) if c.get('type')=='output_text')
        (folder/'output.txt').write_text(text,encoding='utf-8')
        meta.update(response_status=data.get('status'),incomplete_details=data.get('incomplete_details'),resolved_model=data.get('model'),usage=data.get('usage'),final_chars=len(text))
        if data.get('status')!='completed':meta['error']='generation_incomplete'
        elif not text.strip():meta['error']='empty_final_text'
        else:
            parsed=json.loads(re.sub(r'^```(?:json)?\s*|\s*```$','',text.strip()));save(folder/'parsed.json',parsed);meta['status']='returned_json'
    except urllib.error.HTTPError as e:
        meta['error']='http_'+str(e.code);meta['retry_after']=e.headers.get('Retry-After');(folder/'http-error.raw').write_bytes(e.read())
    except Exception as e:meta['error']=type(e).__name__
    meta.update(elapsed=round(time.time()-start,2),prompt_sha256=sha(folder/'prompt.txt'),system_sha256=sha(folder/'system.txt'));save(folder/'metadata.json',meta)
    return meta

class ServiceGate:
    """FIFO, one in-flight request per service, cooldown after each response."""
    def __init__(self,gap=10):
        self.condition=threading.Condition();self.next_ticket=0;self.serving=0;self.ready=0;self.stopped=False;self.gap=gap
    def call(self,route,folder,system,prompt):
        with self.condition:
            ticket=self.next_ticket;self.next_ticket+=1
            while ticket!=self.serving:self.condition.wait()
            if self.stopped:
                self.serving+=1;self.condition.notify_all()
                return {'route':route,'status':'not_attempted','error':'service_stopped_after_429'}
        delay=max(0,self.ready-time.monotonic())
        if delay:time.sleep(delay)
        try:
            result=invoke(route,folder,system,prompt)
            result['gap_after_previous_response_seconds']=self.gap
            if result.get('error')=='http_429':self.stopped=True
            return result
        finally:
            with self.condition:
                self.ready=time.monotonic()+self.gap;self.serving+=1;self.condition.notify_all()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--previous',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--prepare-only',action='store_true');a=ap.parse_args();exp=a.output.resolve();exp.mkdir(parents=True,exist_ok=False)
    selected=['T001','T006','T033','T048','T052','T054'];allcases=read(a.previous/'inputs.json')['revision'];cases=[next(c for c in allcases if c['id']==i) for i in selected]
    routes=read(a.previous/'routes.json')['models']+[{'provider':'ollama','model':m} for m in ['glm-5.2','glm-5.3-flash']]+[{'provider':'codex','model':m} for m in ['gpt-5.5','gpt-5.6-sol','gpt-5.6-terra']]
    base='제공된 원문과 문맥을 바탕으로 자연스러운 한국어 표현을 검토하고 고쳐 주세요. 사실·코드 식별자·조건·범위를 보존하세요. context_before와 context_after는 의미 판단을 위한 참고이며 교정 대상은 target뿐입니다. 도구를 사용하거나 외부 파일을 읽지 마세요. 요청한 JSON만 반환하세요.'
    prompts={
      'diagnosis':'대상 한 건의 표현을 검토하고 아직 수정문은 작성하지 마세요. JSON 객체에 case_id(입력 id와 같은 문자열), decision(issue/none/uncertain), findings(배열)를 반환하세요. 각 finding은 finding_id(문항 내 고유 문자열), quote(target의 정확한 구절), occurrence(동일 구절의 출현 순서, 1부터 시작하는 정수), category(word_choice/collocation/metaphor/other), reason(문맥에 근거한 짧은 설명), judgment(revise/keep/uncertain)를 포함하세요. 문제없으면 findings는 빈 배열입니다. 내부 사고 과정은 요구하지 않습니다.',
      'revision':'같은 원문의 target을 고정 진단에 따라 교정하세요. JSON 객체에 case_id, text(전체 수정문 문자열), actions(배열)를 반환하세요. 각 action은 finding_id, action(revise/keep/clarify), replacement를 포함하세요. revise이면 replacement는 수정 표현 문자열, keep 또는 clarify이면 문자열이나 null을 허용합니다. 모든 기존 finding_id에 대응하세요. 제공된 위치 검사에서 context_only나 not_in_source인 항목은 교정에 사용하지 말고 keep 또는 clarify로 기록하세요. 원진단을 덮어쓰지 마세요. 의미가 불확실하면 추측하지 말고 해당 표현을 유지하세요. 새 발견은 additional_findings에 별도 기록하세요.'}
    skill=(a.previous/'skill-revised.txt').read_text(encoding='utf-8');save(exp/'inputs.json',cases);save(exp/'prompts.json',prompts);(exp/'skill.txt').write_text(skill,encoding='utf-8');(exp/'base.txt').write_text(base,encoding='utf-8')
    plan={'routes':routes,'case_ids':selected,'repetitions':1,'arms':['N','NS'],'max_calls':len(routes)*len(cases)*4,'one_case_per_call':True,'output_limit':'not_set_by_client','http_timeout_seconds':360,'stop_route_on':['http_401','http_403','http_429'],'no_external_judge':True,'selection':'posthoc_purposeful_not_representative','sequence':'case index plus route index parity alternates N/NS; diagnosis then revision within each arm'}
    plan.update(service_concurrency=1,service_gap_seconds=10,stop_whole_service_on_429=True,consecutive_failure_stop=3)
    save(exp/'plan.json',plan);save(exp/'freeze.json',{'files':{p.name:sha(p) for p in exp.iterdir() if p.is_file()},'runner_sha256':sha(Path(__file__)),'cli_adapter_sha256':sha(Path(__file__).with_name('run_lexical_v10_once.py'))})
    if a.prepare_only:
        print('Prepared exact inputs and requests; no external calls.');return
    gates={provider:ServiceGate() for provider in {r['provider'] for r in routes}}
    def worker(index_route):
        ri,route=index_route;rows=[];stop=False;failures=0
        for ci,case in enumerate(cases):
            for arm in (['N','NS'] if (ci+ri)%2==0 else ['NS','N']):
                if stop:break
                root=exp/'runs'/route['model'].replace(':','-')/case['id']/arm;system=base+('\n\n'+skill if arm=='NS' else '')
                prompt=prompts['diagnosis']+'\n'+json.dumps(case,ensure_ascii=False);meta=gates[route['provider']].call(route,root/'diagnosis',system,prompt);rows.append(meta)
                if meta['status']=='not_attempted':stop=True;break
                if meta.get('error') in plan['stop_route_on']:stop=True
                if meta['status']=='returned_json':
                    d=read(root/'diagnosis/parsed.json');check=check_diagnosis(case,d);save(root/'diagnosis/validation.json',check)
                    if check['usable']:
                        save(root/'diagnosis/locked.json',{'sha256':sha(root/'diagnosis/parsed.json')})
                        prompt=prompts['revision']+'\n원문:\n'+json.dumps(case,ensure_ascii=False)+'\n고정 진단:\n'+json.dumps(d,ensure_ascii=False)+'\n위치 검사:\n'+json.dumps(check,ensure_ascii=False)
                        meta=gates[route['provider']].call(route,root/'revision',system,prompt);rows.append(meta)
                        if meta['status']=='not_attempted':stop=True;break
                        if meta.get('error') in plan['stop_route_on']:stop=True
                        if meta['status']=='returned_json':save(root/'revision/validation.json',check_revision(d,read(root/'revision/parsed.json')))
                failures=failures+1 if meta['status']!='returned_json' else 0
                if failures>=3:stop=True
                print(json.dumps({'model':route['model'],'case':case['id'],'arm':arm,'last_status':meta['status'],'error':meta.get('error'),'route_stopped':stop}),flush=True)
            if stop:break
        save(exp/('route-'+route['model'].replace(':','-')+'.json'),{'attempts':rows,'stopped':stop});return rows
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(routes)) as pool:results=list(pool.map(worker,enumerate(routes)))
    save(exp/'summary.json',results)

if __name__=='__main__':main()
