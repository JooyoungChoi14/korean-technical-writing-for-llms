"""Validate explicit diagnostic records without treating them as internal reasoning."""
import argparse
import hashlib
import json
from pathlib import Path


def validate_diagnosis(source, record, case_id):
    assert record['case_id'] == case_id
    assert record['decision'] in {'issue', 'none', 'uncertain'}
    findings = record['findings']
    assert isinstance(findings, list)
    assert len({f['finding_id'] for f in findings}) == len(findings)
    if record['decision'] == 'none':
        assert not findings
    if record['decision'] == 'issue':
        assert findings
    for finding in findings:
        quote = finding['quote']
        assert isinstance(quote, str) and quote
        occurrence = finding['occurrence']
        assert type(occurrence) is int and 1 <= occurrence <= source.count(quote)
        assert finding['category'] in {'word_choice', 'collocation', 'metaphor', 'other'}
        assert finding['judgment'] in {'revise', 'keep', 'uncertain'}
        assert isinstance(finding['reason'], str) and finding['reason'].strip()


def validate_revision(diagnosis, record):
    assert record['case_id'] == diagnosis['case_id']
    assert isinstance(record['text'], str) and record['text'].strip()
    actions = record['actions']
    ids = [a['finding_id'] for a in actions]
    assert len(ids) == len(set(ids))
    assert set(ids) == {f['finding_id'] for f in diagnosis['findings']}
    for action in actions:
        assert action['action'] in {'revise', 'keep', 'clarify'}
        assert isinstance(action['replacement'], str)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--experiment', type=Path, required=True)
    args = parser.parse_args()
    exp = args.experiment
    freeze = json.loads((exp / 'freeze.json').read_text(encoding='utf-8'))
    for name, digest in freeze['files'].items():
        assert hashlib.sha256((exp / name).read_bytes()).hexdigest() == digest, name
    source = '정책을 착지시킨다.'
    good = {'case_id': 'test', 'decision': 'issue', 'findings': [{'finding_id': 'F1', 'quote': '착지시킨다', 'occurrence': 1, 'category': 'metaphor', 'reason': '문맥에서 동작 확인 필요', 'judgment': 'uncertain'}]}
    validate_diagnosis(source, good, 'test')
    validate_revision(good, {'case_id': 'test', 'text': source, 'actions': [{'finding_id': 'F1', 'action': 'clarify', 'replacement': ''}]})
    for quote, occurrence in [('원문에 없는 구절', 1), ('착지시킨다', 2)]:
        bad = json.loads(json.dumps(good))
        bad['findings'][0].update(quote=quote, occurrence=occurrence)
        try:
            validate_diagnosis(source, bad, 'test')
        except AssertionError:
            pass
        else:
            raise AssertionError('Invalid source location accepted')
    try:
        validate_revision(good, {'case_id': 'test', 'text': source, 'actions': []})
    except AssertionError:
        pass
    else:
        raise AssertionError('Missing finding/action link accepted')
    print('Frozen files and diagnostic validation checks passed; no model calls made.')


if __name__ == '__main__':
    main()
