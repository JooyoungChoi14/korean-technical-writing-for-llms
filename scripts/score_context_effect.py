#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from collections import defaultdict
from pathlib import Path

def text(v): return "" if v is None else re.sub(r"\s+", " ", str(v)).strip()

def parse(raw):
    raw=raw.lstrip("\ufeff").strip()
    m=re.fullmatch(r"```(?:json)?\s*(.*?)\s*```",raw,re.S|re.I)
    if m: raw=m.group(1)
    try:return json.loads(raw)
    except json.JSONDecodeError:
        return json.loads(raw[raw.find('{'):raw.rfind('}')+1])

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--tasks',type=Path,required=True); ap.add_argument('--results',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args()
    tasks=json.loads(a.tasks.read_text(encoding='utf-8-sig')); byid={c['id']:c for c in tasks['cases']}; rows=[]
    for meta_path in sorted(p for p in a.results.rglob('run-*.json') if re.fullmatch(r'run-\d+\.json',p.name)):
        meta=json.loads(meta_path.read_text(encoding='utf-8-sig')); out=meta_path.with_suffix('.md'); row={k:meta.get(k) for k in ['model','variant','context_condition','run','transport_status','elapsed_seconds']}; row.update(json_valid=False,case_count_valid=False,cases=[],error=None)
        raw=out.read_text(encoding='utf-8-sig') if out.exists() else ''
        if not raw.strip(): row['error']='empty'; rows.append(row); continue
        try: answers=parse(raw).get('cases',[]); row['json_valid']=isinstance(answers,list)
        except Exception as e: row['error']=f'json: {e}'; rows.append(row); continue
        expected=[c for c in tasks['cases'] if c['context_condition']==meta['context_condition']]; ans={str(x.get('id')):x for x in answers if isinstance(x,dict)}; row['case_count_valid']=set(ans)=={c['id'] for c in expected} and len(answers)==len(expected)
        for c in expected:
            x=ans.get(c['id'],{}); decision=text(x.get('decision')); quote=text(x.get('evidence_quote')); revision=text(x.get('suggested_revision')); question=text(x.get('verification_question')); combined=' '.join([revision,question])
            decision_ok=decision==c['expected_decision']; evidence_exact=bool(quote) and quote in c['context']; evidence_anchor=any(t in quote for t in c['required_evidence_terms'])
            qterms=c.get('required_question_terms',[]); question_ok=(not qterms and not question) or (bool(question) and all(t in question for t in qterms))
            rterms=c.get('required_revision_terms',[]); revision_ok=(not rterms and not revision) or (bool(revision) and all(t in revision for t in rterms))
            forbidden=[t for t in c.get('forbidden_assumptions',[]) if t in combined]; safe=not forbidden
            vals=[decision_ok,evidence_exact,question_ok,revision_ok,safe]
            row['cases'].append({'id':c['id'],'scenario':c['scenario'],'condition':c['context_condition'],'decision_ok':decision_ok,'evidence_exact':evidence_exact,'evidence_anchor':evidence_anchor,'question_ok':question_ok,'revision_ok':revision_ok,'assumption_safe':safe,'forbidden_found':forbidden,'earned':sum(vals),'possible':len(vals)})
        rows.append(row)
    groups=defaultdict(lambda:defaultdict(int)); model_groups=defaultdict(lambda:defaultdict(int))
    for r in rows:
        targets=[groups[(r['variant'],r['context_condition'])],model_groups[(r['model'],r['variant'],r['context_condition'])]]
        for g in targets:g['runs']+=1; g['completed']+=int(r['transport_status']=='completed'); g['json_valid']+=int(r['json_valid'])
        for c in r['cases']:
            for g in targets:g['earned']+=c['earned'];g['possible']+=c['possible'];g['decision_ok']+=c['decision_ok'];g['cases']+=1;g['grounded']+=c['evidence_exact'];g['anchor_match']+=c['evidence_anchor'];g['safe']+=c['assumption_safe'];g['question_ok']+=c['question_ok'];g['revision_ok']+=c['revision_ok']
    def metrics(g):
        return {**g,'completion_rate':round(g['completed']/g['runs'],4),'score':round(g['earned']/g['possible'],4) if g['possible'] else 0,'decision_accuracy':round(g['decision_ok']/g['cases'],4) if g['cases'] else 0,'grounding_rate':round(g['grounded']/g['cases'],4) if g['cases'] else 0,'anchor_match_rate':round(g['anchor_match']/g['cases'],4) if g['cases'] else 0,'assumption_safe_rate':round(g['safe']/g['cases'],4) if g['cases'] else 0,'question_accuracy':round(g['question_ok']/g['cases'],4) if g['cases'] else 0,'revision_accuracy':round(g['revision_ok']/g['cases'],4) if g['cases'] else 0}
    summary=[]
    for (v,cond),g in sorted(groups.items()):
        summary.append({'variant':v,'context_condition':cond,**metrics(g)})
    per_model=[{'model':m,'variant':v,'context_condition':cond,**metrics(g)} for (m,v,cond),g in sorted(model_groups.items())]
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps({'records':rows,'summary':summary,'per_model':per_model},ensure_ascii=False,indent=2),encoding='utf-8');print(f'Scored {len(rows)} outputs')
if __name__=='__main__':main()
