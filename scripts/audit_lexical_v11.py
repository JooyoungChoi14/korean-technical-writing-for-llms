"""Verify frozen inputs, provider spacing, and validation records without calls."""
import argparse, collections, hashlib, json
from pathlib import Path

def read(path): return json.loads(path.read_text(encoding='utf-8'))
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--experiment',type=Path,required=True);exp=ap.parse_args().experiment
    freeze=read(exp/'freeze.json');scripts=Path(__file__).resolve().parent
    for name,digest in freeze['files'].items(): assert sha(exp/name)==digest,name
    assert sha(scripts/'run_lexical_v11.py')==freeze['runner_sha256']
    assert sha(scripts/'run_lexical_v10_once.py')==freeze['cli_adapter_sha256']
    groups=collections.defaultdict(list);errors=collections.Counter();validations=collections.Counter();requests=0
    for path in (exp/'runs').glob('*/*/*/*/metadata.json'):
        m=read(path);folder=path.parent
        groups[m['route']['provider']].append((m.get('started',(folder/'prompt.txt').stat().st_mtime),path.stat().st_mtime))
        if m.get('error'): errors[m['error']]+=1
        if (folder/'request.json').exists():
            body=read(folder/'request.json');assert 'max_output_tokens' not in body;requests+=1
        if (folder/'validation.json').exists():
            v=read(folder/'validation.json')
            if not v['usable']:validations['unusable']+=1
            validations.update(v.get('action_errors',[]))
    timing={}
    for provider,rows in groups.items():
        rows.sort();gaps=[b[0]-a[1] for a,b in zip(rows,rows[1:])]
        timing[provider]={'completed':len(rows),'minimum_observed_gap_seconds':round(min(gaps),3),'gaps_below_9_9_seconds':sum(g<9.9 for g in gaps)}
        assert all(g>=9.9 for g in gaps),provider
    result={'frozen_inputs_and_runners_unchanged':True,'timing':timing,'timing_precision_note':'Filesystem timestamps; 0.1s tolerance for timestamp precision.','ollama_requests_without_client_output_limit':requests,'errors':dict(errors),'http_429':errors['http_429'],'validation_errors':dict(validations)}
    (exp/'execution-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False))

if __name__=='__main__':main()
