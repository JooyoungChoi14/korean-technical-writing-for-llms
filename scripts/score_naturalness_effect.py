#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from collections import defaultdict
from pathlib import Path

def norm(value):
    return "" if value is None else re.sub(r"\s+", " ", str(value)).strip()

def parse(raw):
    raw=raw.lstrip("\ufeff").strip()
    fenced=re.fullmatch(r"```(?:json)?\s*(.*?)\s*```",raw,re.S|re.I)
    if fenced: raw=fenced.group(1)
    try: return json.loads(raw)
    except json.JSONDecodeError: return json.loads(raw[raw.find('{'):raw.rfind('}')+1])

def metrics(group):
    cases=group['cases']
    return {
        **group,
        'completion_rate': round(group['completed']/group['runs'],4) if group['runs'] else 0,
        'decision_accuracy': round(group['decision_ok']/cases,4) if cases else 0,
        'edit_behavior_accuracy': round(group['edit_behavior_ok']/cases,4) if cases else 0,
        'awkward_removal_rate': round(group['awkward_removed']/group['awkward_cases'],4) if group['awkward_cases'] else 0,
        'semantic_coverage_rate': round(group['semantic_coverage']/group['awkward_cases'],4) if group['awkward_cases'] else 0,
        'semantic_safety_rate': round(group['assumption_safe']/group['awkward_cases'],4) if group['awkward_cases'] else 0,
        'successful_rewrite_rate': round(group['rewrite_success']/group['awkward_cases'],4) if group['awkward_cases'] else 0,
        'control_precision': round(group['control_ok']/group['control_cases'],4) if group['control_cases'] else 0,
    }

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--tasks',type=Path,required=True);ap.add_argument('--results',type=Path,nargs='+',required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--coverage-mode',choices=['exact','patterns'],default='patterns');a=ap.parse_args()
    tasks=json.loads(a.tasks.read_text(encoding='utf-8-sig'));byid={c['id']:c for c in tasks['cases']};expected_ids=set(byid);rows=[]
    meta_paths=[]
    for result_root in a.results:
        meta_paths.extend(p for p in result_root.rglob('run-*.json') if re.fullmatch(r'run-\d+\.json',p.name))
    for meta_path in sorted(meta_paths):
        meta=json.loads(meta_path.read_text(encoding='utf-8-sig'));out=meta_path.with_suffix('.md');row={k:meta.get(k) for k in ['agent','model','key','variant','run','transport_status','elapsed_seconds']};row.update(json_valid=False,case_count_valid=False,cases=[],error=None)
        raw=out.read_text(encoding='utf-8-sig') if out.exists() else ''
        if not raw.strip():row['error']='empty';rows.append(row);continue
        try: answers=parse(raw).get('cases',[]);row['json_valid']=isinstance(answers,list)
        except Exception as exc:row['error']=f'json: {exc}';rows.append(row);continue
        answer_map={str(x.get('id')):x for x in answers if isinstance(x,dict)};row['case_count_valid']=set(answer_map)==expected_ids and len(answers)==len(expected_ids)
        for case in tasks['cases']:
            answer=answer_map.get(case['id'],{});decision=norm(answer.get('decision'));revision=norm(answer.get('suggested_revision'));kind=case['kind']
            decision_ok=decision==case['expected_decision'];edit_behavior_ok=bool(revision) if kind=='awkward' else not revision
            banned_found=[term for term in case['banned_phrases'] if term.lower() in revision.lower()]
            required_patterns=case.get('required_patterns',[re.escape(term) for term in case['required_terms']]) if a.coverage_mode=='patterns' else [re.escape(term) for term in case['required_terms']]
            missing_required=[pattern for pattern in required_patterns if not re.search(pattern,revision,re.I)]
            forbidden_found=[term for term in case['forbidden_assumptions'] if term.lower() in revision.lower()]
            awkward_removed=kind!='awkward' or (bool(revision) and not banned_found and norm(revision)!=norm(case['target']))
            semantic_coverage=kind!='awkward' or (bool(revision) and not missing_required)
            assumption_safe=kind!='awkward' or not forbidden_found
            rewrite_success=kind=='awkward' and decision_ok and edit_behavior_ok and awkward_removed and semantic_coverage and assumption_safe
            control_ok=kind=='control' and decision_ok and edit_behavior_ok
            row['cases'].append({'id':case['id'],'kind':kind,'category':case['category'],'decision':decision,'suggested_revision':revision,'reason':norm(answer.get('reason')),'decision_ok':decision_ok,'edit_behavior_ok':edit_behavior_ok,'awkward_removed':awkward_removed,'semantic_coverage':semantic_coverage,'assumption_safe':assumption_safe,'rewrite_success':rewrite_success,'control_ok':control_ok,'banned_found':banned_found,'missing_required':missing_required,'forbidden_found':forbidden_found})
        rows.append(row)
    groups=defaultdict(lambda:defaultdict(int));model_groups=defaultdict(lambda:defaultdict(int));category_groups=defaultdict(lambda:defaultdict(int))
    for row in rows:
        targets=[groups[row['variant']],model_groups[(row['model'],row['variant'])]]
        for group in targets:group['runs']+=1;group['completed']+=int(row['transport_status']=='completed');group['json_valid']+=int(row['json_valid'])
        for category in {case['category'] for case in row['cases']}:
            group=category_groups[(category,row['variant'])];group['runs']+=1;group['completed']+=int(row['transport_status']=='completed');group['json_valid']+=int(row['json_valid'])
        for case in row['cases']:
            case_targets=targets+[category_groups[(case['category'],row['variant'])]]
            for group in case_targets:
                group['cases']+=1;group['decision_ok']+=case['decision_ok'];group['edit_behavior_ok']+=case['edit_behavior_ok']
                if case['kind']=='awkward':
                    group['awkward_cases']+=1;group['awkward_removed']+=case['awkward_removed'];group['semantic_coverage']+=case['semantic_coverage'];group['assumption_safe']+=case['assumption_safe'];group['rewrite_success']+=case['rewrite_success']
                else:group['control_cases']+=1;group['control_ok']+=case['control_ok']
    summary=[{'variant':variant,**metrics(group)} for variant,group in sorted(groups.items())]
    per_model=[{'model':model,'variant':variant,**metrics(group)} for (model,variant),group in sorted(model_groups.items())]
    per_category=[{'category':category,'variant':variant,**metrics(group)} for (category,variant),group in sorted(category_groups.items())]
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps({'coverage_mode':a.coverage_mode,'records':rows,'summary':summary,'per_model':per_model,'per_category':per_category},ensure_ascii=False,indent=2),encoding='utf-8');print(f'Scored {len(rows)} outputs ({a.coverage_mode})')

if __name__=='__main__':main()
