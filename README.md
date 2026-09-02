# Korean Technical Writing for LLMs

LLM이 만든 한국어 기술 문서를 **문법 오류가 아니라 독자가 부담하는 재해석 비용**의 관점에서 검토하는 공개 실험과 Agent Skill입니다.

> 문장이 틀리지 않았더라도, 독자가 비유를 실제 동작으로 바꾸고 생략된 주체·조건·결과를 채워야 한다면 설명의 일부를 독자에게 떠넘긴 셈입니다.

이 저장소에는 다음 결과물이 있습니다.

- [읽는 순서로 구성한 한국어 보고서](report/experiment.ko.md)
- [브라우저에서 바로 읽는 실험 문서](docs/index.html)
- Claude Code와 Codex 등에서 사용할 수 있는 [`korean-technical-writing-review`](plugins/korean-technical-writing-review/skills/korean-technical-writing-review/SKILL.md) 스킬
- 공개 가능한 합성 사례 24개와 기대 판정으로 구성한 [평가 세트](evals/README.md)
- Codex용 플러그인 및 저장소 마켓플레이스 메타데이터

## 가장 짧은 사용법

Agent Skills를 지원하는 CLI에서는 다음 명령으로 설치할 수 있습니다.

```bash
npx skills add JooyoungChoi14/korean-technical-writing-for-llms --skill korean-technical-writing-review
```

설치 뒤에는 다음처럼 요청합니다.

```text
$korean-technical-writing-review 이 설계 문서를 검사하고, 의미를 확정할 수 있는 문장만 제한적으로 고쳐 주세요.
```

Codex 저장소 플러그인으로 사용할 때는 `.agents/plugins/marketplace.json`과 `plugins/`를 함께 사용합니다.

## 핵심 제안

1. **작성·재작성:** 원문 표현이 아니라 사실, 코드 식별자, 문서 구조를 보존합니다.
2. **검사:** 비유, 혼합어, 명사 나열 자체를 금지하지 않고 그 때문에 대상이나 동작이 빠졌는지 찾습니다.
3. **제한 교정:** 검사에서 표시된 문장만 고칩니다. 확정할 수 없는 뜻은 창작하지 않고 `[확인 필요]`로 남깁니다.
4. **의미 검증:** 자연스러움과 사실 보존을 별도로 판정합니다.

이 방식은 특정 모델을 판별하거나 비난하기 위한 것이 아닙니다. 생성 도구와 관계없이 문서가 독자에게 요구하는 추론을 줄이기 위한 편집 절차입니다.

## 연구 범위

초기 탐색에서는 비공개 프로젝트의 Markdown·HTML 200개를 검토해 후보 40개를 분류하고, 비공개 발췌본 2편에 다섯 가지 지침을 각각 한 번 적용했습니다. 공개 저장소에는 원문·프로젝트명·조직 정보 대신 같은 현상을 재현하는 합성 사례만 포함합니다. 결과는 통계적 모델 비교가 아니라 하네스 설계를 위한 탐색적 관찰입니다.

## 저자와 기여

문제 정의, 자료 선정, 실험 설계, 평가 기준, 사실 검증, 결론 및 최종 편집: **최주영 (Jooyoung Choi, [@JooyoungChoi14](https://github.com/JooyoungChoi14))**.

AI 시스템은 실험 대상이자 초안·검토 도구로 사용되었습니다. 공개 여부와 최종 판단의 책임은 저자에게 있습니다. 인용 방법은 [`CITATION.cff`](CITATION.cff)를 참고하십시오.

## 라이선스

코드, 스킬, 문서는 [MIT License](LICENSE)로 배포합니다. 사례를 인용할 때는 출처를 밝혀 주세요.
