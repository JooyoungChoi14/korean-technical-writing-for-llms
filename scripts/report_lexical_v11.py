"""Read-only aggregation and deterministic masked review packet for v11."""
import argparse, collections, hashlib, json
from pathlib import Path

def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--experiment',type=Path,required=True);a=ap.parse_args();exp=a.experiment;plan=read(exp/'plan.json');cases=read(exp/'inputs.json');freeze=read(exp/'freeze.json')
    for name,h in freeze['files'].items():assert sha(exp/name)==h,name
    records=[];pairs=[];key=[];diagstats=[]
    for route in plan['routes']:
        root=exp/'runs'/route['model'].replace(':','-');metas=[read(p) for p in root.glob('*/*/*/metadata.json')]
        valid_diags=list(root.glob('*/*/diagnosis/locked.json'));valid_revs=[p for p in root.glob('*/*/revision/validation.json') if read(p)['usable']]
        errors=collections.Counter(m.get('error') for m in metas if m['status']!='returned_json')
        record={'model':route['model'],'provider':route['provider'],'attempts':len(metas),'json_returned':sum(m['status']=='returned_json' for m in metas),'diagnoses':len(valid_diags),'revisions':len(valid_revs),'errors':dict(errors),'paired_revisions':0}
        for case in cases:
            for arm in ['N','NS']:
                droot=root/case['id']/arm/'diagnosis';rroot=root/case['id']/arm/'revision'
                if (droot/'locked.json').exists():
                    assert sha(droot/'parsed.json')==read(droot/'locked.json')['sha256']
                    d=read(droot/'parsed.json');v=read(droot/'validation.json')
                    diagstats.append({'model':route['model'],'case_id':case['id'],'arm':arm,'decision':d['decision'],'locations':dict(collections.Counter(x['location'] for x in v['locations'])),'findings':len(d['findings']),'judgments':dict(collections.Counter(x['judgment'] for x in d['findings']))})
                if (rroot/'parsed.json').exists() and (rroot/'validation.json').exists():
                    for stage in ['diagnosis','revision']:
                        folder=root/case['id']/arm/stage;m=read(folder/'metadata.json')
                        # The adapters hash Unicode strings before writing, so normalize CRLF.
                        for name in ['prompt','system']:
                            path=folder/(name+'.txt')
                            assert m[name+'_sha256'] in {sha(path),hashlib.sha256(path.read_text(encoding='utf-8').encode()).hexdigest()}
            folders=[root/case['id']/arm/'revision' for arm in ['N','NS']]
            if all((f/'validation.json').exists() and read(f/'validation.json')['usable'] for f in folders):
                rid='P'+hashlib.sha256((route['model']+case['id']).encode()).hexdigest()[:10]
                order=['N','NS'] if int(rid[-1],16)%2==0 else ['NS','N']
                outputs={arm:read(root/case['id']/arm/'revision/parsed.json')['text'] for arm in ['N','NS']}
                pairs.append({'pair_id':rid,'case_id':case['id'],'source':case,'A':outputs[order[0]],'B':outputs[order[1]]});key.append({'pair_id':rid,'model':route['model'],'A':order[0],'B':order[1]});record['paired_revisions']+=1
        records.append(record)
    pairs.sort(key=lambda x:x['pair_id']);save(exp/'review-pairs.json',pairs);save(exp/'review-key.json',key);save(exp/'diagnostic-counts.json',diagstats);save(exp/'operational-report.json',records)
    report=['# v11 실제 실행 상태','','N/NS 각 1회, 한 문항씩 진단 후 교정. 출력 한도 미지정. 서비스별 동시 1개·응답 후 10초 간격. 표본은 후보 4개와 대조 2개로 사후 선정했다.','', '| 요청 모델 | 시도 | JSON 반환 | 진단 유효 | 교정 유효 | N/NS 교정 쌍 | 오류 |','|---|---:|---:|---:|---:|---:|---|']
    for r in records:report.append(f"| {r['model']} | {r['attempts']} | {r['json_returned']} | {r['diagnoses']} | {r['revisions']} | {r['paired_revisions']} | {json.dumps(r['errors'])} |")
    report+=['','실행 완료: '+str((exp/'summary.json').exists()),'','유효는 자료형·식별자 검증 기준이며 언어적 정확성을 뜻하지 않는다. 같은 문항·모델에서 두 조건이 모두 있는 쌍만 비교한다. 자료형 오류와 의미·표현 문제는 별도다. 사람 평가 및 외부 모델 채점은 수행하지 않았다.']
    (exp/'status.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
    if (exp/'summary.json').exists():
        packet=['# v11 비공개 원문·진단·교정 전체 결과','','모델명은 요청한 모델이며 서비스 경로와 함께 표시한다. 원문은 외부 공개하지 않는다.','']
        for route in plan['routes']:
            packet+=['## '+route['model']+' / '+route['provider'],'']
            for case in cases:
                packet+=['### '+case['id'],'','원문:',case['target'],'']
                for arm in ['N','NS']:
                    packet+=['#### '+arm,'']
                    for stage in ['diagnosis','revision']:
                        folder=exp/'runs'/route['model'].replace(':','-')/case['id']/arm/stage
                        packet+=[stage+':']
                        if (folder/'parsed.json').exists():packet+=['```json',json.dumps(read(folder/'parsed.json'),ensure_ascii=False,indent=2),'```','']
                        elif (folder/'metadata.json').exists():packet+=[read(folder/'metadata.json').get('error','no parsed output'),'']
                        else:packet+=['미실행','']
        (exp/'all-results.md').write_text('\n'.join(packet)+'\n',encoding='utf-8')
    print(json.dumps({'attempts':sum(r['attempts'] for r in records),'max_calls':plan['max_calls'],'pairs':len(pairs),'finished':(exp/'summary.json').exists(),'errors':{r['model']:r['errors'] for r in records if r['errors']}},ensure_ascii=False))

if __name__=='__main__':main()
