# CLI 설치·동작 스모크 테스트

이 테스트는 공개 GitHub 저장소에서 `korean-technical-writing-review`를 새 프로젝트에 설치했을 때 Claude Code와 Codex CLI가 스킬을 발견하고 핵심 판정 원칙을 적용하는지 확인합니다.

## 확인하려는 것

1. 설치 도구가 공개 저장소에서 스킬을 찾을 수 있는가?
2. 설치된 파일이 테스트 당시 저장소 원본과 같은가?
3. 각 CLI가 프로젝트 로컬 스킬을 발견하는가?
4. 스킬이 모호한 비유, 명확한 설명, 의미 충돌 가능성을 구분하는가?

이 네 항목을 모두 만족하면 설치와 핵심 행동이 작동하는 것으로 판정합니다. 한 번의 실행만으로 모델의 일반 성능이나 통계적 향상을 주장하지 않습니다.

## 테스트 환경

- 날짜: 2026-09-02
- 테스트한 저장소 커밋: `aa308e0`
- Claude Code 2.0.73
  - `sonnet` (`claude-sonnet-4-5-20250929`)
  - `claude-opus-5`
- Codex CLI 0.151.0-alpha.7.2, reasoning effort `medium`
  - `gpt-5.6-sol`
  - `gpt-5.3-codex-spark`
- 설치 위치: 기존 전역 스킬과 분리한 임시 Git 프로젝트

계정 식별자, 인증 정보, 세션 ID와 로컬 절대 경로는 기록하지 않았습니다.

### 추가 모델을 고른 이유

첫 실행은 Claude Sonnet 4.5와 Codex의 고성능 `gpt-5.6-sol` 조합이어서 모델 등급이 대칭적이지 않았습니다. 추가 실행에서는 Claude의 현재 고성능 모델인 `claude-opus-5`와 빠르고 집중된 작업용 Codex-Spark 계열인 `gpt-5.3-codex-spark`를 선택했습니다.

- [Anthropic의 활성 모델 목록](https://platform.claude.com/docs/en/about-claude/model-deprecations)
- [Anthropic의 Claude Code `--model` 설명](https://code.claude.com/docs/en/cli-usage)
- [OpenAI의 Codex-Spark 사용 사례](https://learn.chatgpt.com/use-cases/make-granular-ui-changes)

로컬 Claude Code에서 `--model opus`도 진단 실행했지만 `claude-opus-4-5-20251101`로 해석됐고 3번의 충돌을 놓쳤습니다. 최신 모델 비교라는 목적과 맞지 않아 결과표에서는 제외하되, 실행 사실과 2/3 충족 결과는 [`run-metadata.json`](run-metadata.json)에 남겼습니다. 이후 전체 모델 ID `claude-opus-5`로 다시 실행했습니다.

## 설치

빈 디렉터리에서 Git 저장소를 만든 뒤 다음 명령을 실행했습니다.

```bash
git init
npx -y skills add JooyoungChoi14/korean-technical-writing-for-llms \
  --agent claude-code \
  --agent codex \
  --skill korean-technical-writing-review \
  --yes
npx -y skills list
```

설치 도구는 공용 원본을 `.agents/skills/korean-technical-writing-review`에 두고, Claude Code가 읽는 `.claude/skills/korean-technical-writing-review`를 정션으로 연결했습니다. 설치 목록에는 Claude Code와 Codex가 모두 표시됐습니다.

설치된 `SKILL.md`, `agents/openai.yaml`, 참조 문서 3개를 저장소 원본과 비교했습니다. 줄바꿈을 LF로 정규화한 뒤 5개 파일의 내용이 모두 일치했습니다.

## 입력과 기대 행동

두 CLI에는 [`prompt.ko.txt`](prompt.ko.txt)의 같은 세 문장을 제공했습니다. Claude Code에서는 `/korean-technical-writing-review`, Codex에서는 `$korean-technical-writing-review`를 입력 앞에 붙였습니다.

기대 행동은 [`expected.json`](expected.json)에 기계 판독 가능한 형태로 기록했습니다.

| 사례 | 기대 행동 |
|---|---|
| `그릇` 비유 | 실제 기술 대상을 묻고 임의로 확정하지 않는다. |
| 만료 검사 | 대상·시점·동작이 명확하므로 통과시킨다. |
| 권한 우선순위 | 나열 순서와 거부 우선이 함께 성립하는지 확인한다. |

## 실행

다음 명령의 `$sourceCheckout`에는 이 저장소를 체크아웃한 경로를 지정합니다. CLI 명령은 스킬을 설치한 임시 프로젝트 안에서 실행합니다.

Claude Code에서는 프로젝트 설정만 읽고 `Read`와 `Skill` 도구만 허용했습니다. 빈 MCP 설정을 사용하고 세션을 저장하지 않았습니다.

```powershell
$sourceCheckout = 'C:\path\to\korean-technical-writing-for-llms'
$promptPath = Join-Path $sourceCheckout 'evals\cli-smoke\prompt.ko.txt'
$skillSmokePrompt = '/korean-technical-writing-review' + "`n`n" +
  (Get-Content -Raw -Encoding UTF8 $promptPath)

claude -p $skillSmokePrompt `
  --model sonnet `
  --setting-sources project `
  --allowedTools 'Read,Skill' `
  --permission-mode dontAsk `
  --no-session-persistence `
  --no-chrome `
  --strict-mcp-config `
  --mcp-config '{"mcpServers":{}}' `
  --output-format json
```

Opus 5 실행에서는 나머지 조건을 그대로 두고 모델만 명시적으로 바꿨습니다.

```powershell
claude -p $skillSmokePrompt `
  --model claude-opus-5 `
  --setting-sources project `
  --allowedTools 'Read,Skill' `
  --permission-mode dontAsk `
  --no-session-persistence `
  --no-chrome `
  --strict-mcp-config `
  --mcp-config '{"mcpServers":{}}' `
  --output-format json
```

Codex CLI에서는 읽기 전용 샌드박스와 임시 세션을 사용했습니다.

```powershell
$sourceCheckout = 'C:\path\to\korean-technical-writing-for-llms'
$promptPath = Join-Path $sourceCheckout 'evals\cli-smoke\prompt.ko.txt'
$skillSmokePrompt = '$korean-technical-writing-review' + "`n`n" +
  (Get-Content -Raw -Encoding UTF8 $promptPath)

codex exec `
  --model gpt-5.6-sol `
  --sandbox read-only `
  --ephemeral `
  --ignore-rules `
  --color never `
  $skillSmokePrompt
```

Spark 실행에서도 모델 이외의 조건을 유지했습니다.

```powershell
codex exec `
  --model gpt-5.3-codex-spark `
  -c 'model_reasoning_effort="medium"' `
  --sandbox read-only `
  --ephemeral `
  --ignore-rules `
  --color never `
  $skillSmokePrompt
```

Codex 호출 문자열은 작은따옴표로 감싸 `$`가 PowerShell 변수로 해석되지 않게 했습니다.

## 결과

| 모델 | 스킬 발견 | `그릇`의 대상 확인 | 명확한 문장 통과 | 권한 규칙의 의미 충돌 확인 | 종합 |
|---|---|---|---|---|---|
| Claude Sonnet 4.5 | 통과 | 통과 | 통과 | 통과 | 통과 |
| Claude Opus 5 | 통과 | 통과 | 통과 | 통과 | 통과 |
| gpt-5.6-sol | 통과 | 통과 | 통과 | 통과 | 통과 |
| gpt-5.3-codex-spark | 통과 | 통과 | 통과 | 실패 | 실패 |

- [Claude Sonnet 4.5 실제 출력](outputs/claude-code-sonnet.md)
- [Claude Opus 5 실제 출력](outputs/claude-code-opus-5.md)
- [Codex gpt-5.6-sol 실제 출력](outputs/codex-gpt-5.6-sol.md)
- [Codex gpt-5.3-codex-spark 실제 출력과 실패 판정](outputs/codex-gpt-5.3-codex-spark.md)
- [구조화된 실행 메타데이터](run-metadata.json)

Sonnet 4.5, Opus 5와 gpt-5.6-sol은 세 사례의 필수 행동을 모두 충족했습니다. Opus 5는 3번을 평가 절차의 생략과 우선순위의 충돌로 나누고, `사용자 직접 허용`과 `역할 거부`가 만나는 구체적인 경우까지 제시했습니다.

Spark는 3번이 모호하다는 사실은 찾았습니다. 그러나 원래의 나열 순서를 유지하면서 “거부가 허용보다 우선”이라고 다시 적어 논리적 충돌을 남겼고, 직접 허용과 역할 거부 중 무엇이 이기는지도 묻지 않았습니다. 문제 문장을 찾아냈다는 이유만으로 통과시키지 않고, [`expected.json`](expected.json)의 필수 행동을 충족하지 못한 것으로 판정했습니다.

첫 Claude 진단 실행에서는 허용 도구를 `Read`로만 제한해 `Skill` 호출이 거부됐습니다. 이 실행은 성공 결과에서 제외했습니다. `Read,Skill`로 바로잡은 실행에는 권한 거부가 없었습니다. 따라서 Claude Code로 재현할 때는 `Skill` 도구를 차단하지 않아야 합니다.

Windows 터미널에 표시된 Codex 도구 실행 로그에서는 한국어 참조 문서가 깨져 보였지만, CLI가 저장한 최종 UTF-8 출력은 정상적이었습니다. 이는 설치 결과가 아니라 터미널 표시 계층의 문제로 기록합니다.

## 이 결과로 말할 수 없는 것

- 스킬 적용 시 모든 한국어 기술 문서의 품질이 향상된다고 일반화할 수 없습니다.
- Claude Code와 Codex의 상대적인 한국어 성능을 비교할 수 없습니다.
- 각 모델 구성을 한 번씩 실행했으므로 출력 변동성과 재현율을 추정할 수 없습니다.
- 스킬 미적용 조건과 통제된 반복 비교를 하지 않았으므로 성능 향상의 크기를 계산할 수 없습니다.

후속 성능 실험에서는 동일한 합성 사례를 스킬 미적용·적용 조건으로 여러 번 실행하고, 모델명을 가린 평가자가 탐지율·오탐률·의미 변경률을 비교해야 합니다.
