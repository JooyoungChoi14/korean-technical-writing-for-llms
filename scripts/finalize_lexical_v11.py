"""Publish only aggregates, retaining source text and review notes privately."""
import argparse, collections, json
from pathlib import Path

def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--experiment',type=Path,required=True);a=ap.parse_args();exp=a.experiment
    assert (exp/'summary.json').exists(),'Execution has not finished'
    records=read(exp/'operational-report.json');pairs={x['pair_id']:x for x in read(exp/'review-pairs.json')};keys={x['pair_id']:x for x in read(exp/'review-key.json')};reviews=read(exp/'local-review.json')['reviews']
    assert len({x['pair_id'] for x in reviews})==len(reviews)
    assert {x['pair_id'] for x in reviews}==set(pairs),'Every available pair must be reviewed'
    scored=[]
    for r in reviews:
        pair=pairs[r['pair_id']];key=keys[r['pair_id']];pref=r['preference'];winner=key[pref]+'_better' if pref in ['A','B'] else pref
        scored.append({'model':key['model'],'case_id':pair['case_id'],'kind':'control' if pair['case_id'] in ['T052','T054'] else 'candidate','expression':winner,'meaning_N':r['meaning_A'] if key['A']=='N' else r['meaning_B'],'meaning_NS':r['meaning_A'] if key['A']=='NS' else r['meaning_B']})
    counts={kind:dict(collections.Counter(x['expression'] for x in scored if x['kind']==kind)) for kind in ['candidate','control']}
    diagnostics=read(exp/'diagnostic-counts.json');locs=collections.Counter()
    for d in diagnostics:locs.update(d['locations'])
    result={'status':'execution_complete','attempts':sum(r['attempts'] for r in records),'max_planned_calls':240,'json_returned':sum(r['json_returned'] for r in records),'paired_revisions':len(pairs),'routes':records,'provisional_expression_counts':counts,'location_counts':dict(locs),'human_reviewers':0,'independent_evaluator':False,'limitations':['Purposefully selected four candidates and two controls; not representative.','One repetition; route and temporal variation remain.','Diagnostic scaffolding shared across N/NS; results apply to this workflow.','Expression assessment separate from fidelity; not a general success rate.']}
    result['provisional_fidelity_counts']={arm:dict(collections.Counter(x['meaning_'+arm] for x in scored if x['kind']=='candidate')) for arm in ['N','NS']}
    result['control_fidelity_counts']={arm:dict(collections.Counter(x['meaning_'+arm] for x in scored if x['kind']=='control')) for arm in ['N','NS']}
    result['preferred_expression_with_fidelity_preserved']={arm:sum(x['kind']=='candidate' and x['expression']==arm+'_better' and x['meaning_'+arm]=='preserved' for x in scored) for arm in ['N','NS']}
    result['diagnostic_decisions']={kind:{arm:dict(collections.Counter(d['decision'] for d in diagnostics if d['arm']==arm and (d['case_id'] in ['T052','T054'])==(kind=='control'))) for arm in ['N','NS']} for kind in ['candidate','control']}
    result['candidate_counts_by_model']={r['model']:dict(collections.Counter(x['expression'] for x in scored if x['model']==r['model'] and x['kind']=='candidate')) for r in records}
    result['limitations']+=['The same four candidate items repeat across models; pairs are not independent items.','NS appends skill text; automatic skill discovery or loading was not tested.','Some candidate vocabulary and an exact exclusion control appear in the skill examples.','Claude CLI reported auxiliary model usage; Codex resolved model not independently verified.']
    result['execution_audit']=read(exp/'execution-audit.json')
    repo=Path(__file__).resolve().parents[1]/'evals/lexical-expression-v11';save(repo/'results-summary.json',result);save(exp/'decoded-review.json',scored)
    lines=[(exp/'status.md').read_text(encoding='utf-8'),'\n## 현재 작업의 잠정 평가\n','외부 사람 평가 없이 현재 작업 Astra가 모든 확보 쌍을 검토했다. 모델·조건을 가린 패킷을 만들었지만 실행 맥락을 아는 검토이므로 독립·맹검 평가라고 부르지 않는다.','', '| 구분 | N 우세 | NS 우세 | 동률 | 판단 유보 |','|---|---:|---:|---:|---:|']
    for kind,label in [('candidate','후보'),('control','대조문')]:
        c=counts[kind];lines.append(f"| {label} | {c.get('N_better',0)} | {c.get('NS_better',0)} | {c.get('tie',0)} | {c.get('uncertain',0)} |")
    lines+=['','이 표는 선정된 핵심 어휘의 상대적 자연스러움에 관한 가검토다. 의미 보존을 보장하는 성공률이 아니며 일반 문장 다듬기는 개선으로 세지 않았다. 의미 위험·유보는 비공개 문항별 검토에 별도 기록했다.','',f'위치 검사 집계: {json.dumps(dict(locs),ensure_ascii=False)}.','', 'N과 NS의 차이는 진단과 교정을 포함한 이 작업 흐름에서 관찰한 차이다. 생성 예방 효과, 모델의 일반적 우열, 외부 독자 합의를 입증하지 않는다.']
    lines+=['','후보 의미 보존 가검토 집계: '+json.dumps(result['provisional_fidelity_counts'],ensure_ascii=False),'','어휘 우세이면서 우세 출력의 의미 보존도 통과한 후보 쌍: '+json.dumps(result['preferred_expression_with_fidelity_preserved'],ensure_ascii=False)]
    lines+=['','대조문 의미 보존 가검토 집계: '+json.dumps(result['control_fidelity_counts'],ensure_ascii=False),'','대조문이 어휘 비교에서 동률이라는 것은 출력이 모두 같거나 의미 위험도 없다는 뜻이 아니다. 범위 밖 축약 보완은 어휘 개선으로 세지 않았고 의미 변화 가능성은 따로 기록했다.']
    lines+=['','## 모델이 반환한 진단 판정','','| 구분 | 조건 | issue | uncertain | none |','|---|---|---:|---:|---:|']
    for kind,label in [('candidate','후보'),('control','대조문')]:
        for arm in ['N','NS']:
            c=result['diagnostic_decisions'][kind][arm];lines.append(f"| {label} | {arm} | {c.get('issue',0)} | {c.get('uncertain',0)} | {c.get('none',0)} |")
    lines+=['','유효 진단 전체의 문항 단위 판정이며, 교정 쌍이 없는 진단도 포함한다. 모델의 자기 판정 분포이지 정답과 대조한 탐지 정확도가 아니다. 구체적 판단과 대응의 차이는 [진단 관찰](diagnostic-observations.md)에 기록했다.']
    lines+=['','## 요청 모델별 후보 어휘 비교','','| 요청 모델 | N 우세 | NS 우세 | 동률 | 판단 유보 |','|---|---:|---:|---:|---:|']
    for model,c in result['candidate_counts_by_model'].items():lines.append(f"| {model} | {c.get('N_better',0)} | {c.get('NS_better',0)} | {c.get('tie',0)} | {c.get('uncertain',0)} |")
    lines+=['','모델당 후보는 최대 4쌍이다. 실패로 비교 쌍이 없는 문항은 패배나 동률로 넣지 않았다. 서비스와 전달 방식이 달라 이 표로 모델 순위를 정하지 않는다.']
    lines+=['','## 실행 검증','','입력·실행기 해시가 실행 시작 때와 같고, 검증된 Ollama 요청 142건 모두 클라이언트 출력 한도 필드가 없었다. 서비스별 기록 간격은 약 10초 이상이었다. 429는 0건이며, 파싱된 응답의 문항·자료형·대응 식별자 검증 오류도 없었다.','', '파싱 오류 2건의 원인과 사후 복구는 [응답 처리 관찰](operational-observations.md), 해석과 한계는 [결과 해석](interpretation.md)을 참고한다.']
    (repo/'results.md').write_text('\n'.join(lines)+'\n',encoding='utf-8');print(json.dumps(result,ensure_ascii=False))

if __name__=='__main__':main()
