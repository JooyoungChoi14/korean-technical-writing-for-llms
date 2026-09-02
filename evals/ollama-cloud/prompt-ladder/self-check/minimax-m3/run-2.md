<think>릇" (container/vessel) is a metaphor replacing an actual operation
- What is being discussed? Permissions need to be stored somewhere - a type, class, structure, database column, etc.
- The reader has to infer: What kind of "그릇"? Data structure? Type? Variable? Permission object? Token?
- The rubric explicitly flags this: "동작을 대신하는 비유" - metaphors like 손잡이, 관문, 뼈대, 껍데기 that describe operations through objects
- Verdict: 구체화 필요 (needs specification)
- Suggested revision: Need to know what the actual type/structure is. Could say something like "권한을 저장할 타입이 필요합니다" or "권한 정보를 보관할 데이터 구조가 필요합니다" - but we don't know the actual name
- Facts to verify: What is the actual entity being created? A class? A type? A field?

**Sentence 2: "임시 권한은 만료 시각을 저장하고 각 요청에서 현재 시각과 비교해 유효성을 확인합니다."**
- This is fairly clear: temporary permissions store an expiration time, and at each request compare against current time to verify validity
- Target: 임시 권한 (temporary permission)
- Operation: 만료 시각 저장, 현재 시각과 비교, 유효성 확인
- Conditions: 각 요청에서
- This sentence seems to provide target, operation, and condition
- Verdict: 통과 (pass)

Wait, let me reconsider. "임시 권한" - is this a code identifier or a description? If it's a code type name, it should be preserved as is. But the sentence reads like prose description. The structure is clear: it stores expiration time, compares with current time on each request, and verifies validity.

Actually, this seems pretty clear. The target is "임시 권한", the operations are clearly stated (만료 시각 저장, 비교, 유효성 확인), the condition is "각 요청에서", and the result is implicit (유효성 확인). I think this passes.

**Sentence 3: "사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 적용해 거부를 우선합니다."**
- "사용자 직접 거부" vs "역할 거부" - the word "직접" (direct) appears with "사용자" but not with "역할". This is asymmetric.
- Wait, let me re-read: "사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 적용해 거부를 우선합니다."
- The list is in order of application: user direct deny, user direct allow, role deny, role allow
- "거부를 우선합니다" - denials take priority
- The target/operation seems clear enough: an evaluation order for permission decisions
- But "사용자 직접 거부" - what does "직접" mean here? It's opposed to "역할 거부" (role deny), implying these are user-set denials vs role-based denials
- The "순으로 적용해 거부를 우선합니다" - applies in this order, with denials prioritized

Hmm, let me think about this. The order says "사용자 직접 거부 → 사용자 직접 허용 → 역할 거부 → 역할 허용" and "거부를 우선합니다" means deny takes priority. So in this list, the two deny options come first in the list, and the two allow options come later. That's saying "apply in this order, with denials prioritized."

But the order itself is a bit ambiguous. If denials are prioritized, then shouldn't we check user-deny first, then user-allow, then role-deny, then role-allow? Or is the "순으로 적용해 거부를 우선" implying that within each level (user vs role), deny comes first?

Actually, re-reading: the four items are listed in order. "거부를 우선합니다" might be a summary statement meaning "denials win over allows" rather than "denials come first in the order". The list ordering already puts denies first, so "거부를 우선합니다" might be redundant or might mean something different.

Or perhaps the meaning is: the order is user-deny, user-allow, role-deny, role-allow. Within this order, denies are evaluated/promoted above allows? Or all four are checked in order, and any deny beats any allow?

Let me think again. The sentence says the order is:
1. 사용자 직접 거부
2. 사용자 직접 허용
3. 역할 거부
4. 역할 허용

"적용해 거부를 우선합니다" - apply (in this order) and prioritize denials.

The reader has to infer: does "거부를 우선" mean that any denial (from user or role) beats any allow? Or does it mean denials are checked first within each level?

Also, "사용자 직접 거부" vs "역할 거부" - the word "직접" only appears with "사용자". This might be intentional (distinguishing user-set from role-set) but it's asymmetric in expression. The reader might wonder: why is "직접" only for user? Is there also "역할 직접 거부"? The asymmetry suggests "역할 거부" is the direct one and "사용자" can be direct or inherited... but that doesn't quite fit either.

Actually, this might be just a stylistic asymmetry. In permission systems, there's often:
- User-level direct permissions
- Role-based permissions

"직접" emphasizes that the user explicitly set this (as opposed to inheriting from a group or default). For roles, "역할 거부" is already direct - the role directly denies.

So the meaning might be clear to someone in the domain. But for a general reader, the asymmetry could cause confusion. The reader must infer: why is "직접" only used with "사용자"?

Let me think about the verdict:
- The order of application is stated
- The denial priority is stated
- But the relationship between "거부를 우선" and the list ordering is ambiguous: does any deny beat any allow (including role-allow beating user-deny? no, that contradicts "거부를 우선")?

I think there's ambiguity in whether:
1. "거부를 우선" means "deny wins over allow regardless of source" 
2. The listed order is the evaluation order AND denies are always preferred

If user-deny and role-allow both apply, "거부를 우선" suggests user-deny wins (because it's a deny). This is a specific interpretation that the reader has to infer.

Also, the asymmetry of "직접" is something the reader has to figure out.

Verdict: 구체화 필요 (or maybe 의미 확인 필요 for the priority relationship)

Actually, let me reconsider. The sentence is fairly standard in Korean RBAC documentation. Let me think about whether it really needs revision.

The structure:
- 4 cases listed in order
- "적용해" connects to "거부를 우선"
- "거부를 우선" = prioritize denials

The reader must infer:
- Whether "거부를 우선" is a tie-breaker rule (e.g., user-deny beats role-allow) or just emphasizes that deny entries come first in the list
- Why "직접" is asymmetric

I'd say: 구체화 필요 - the meaning is mostly clear but there's ambiguity in the priority rule and the asymmetry of "직접".

Let me also reconsider sentence 2 more carefully:
"임시 권한은 만료 시각을 저장하고 각 요청에서 현재 시각과 비교해 유효성을 확인합니다."

- Target: 임시 권한
- Operations: 만료 시각 저장, 비교, 유효성 확인
- Conditions: 각 요청에서
- Direction: clear - stores expiration, compares with current, verifies validity

This is pretty clear. I think it passes.

But wait - "임시 권한" could be a code identifier (a type name). If so, it should be preserved. The sentence reads like a description of behavior, which is appropriate.

I think sentence 2 passes.

Now let me also reconsider sentence 1:
"권한을 담아낼 그릇이 필요합니다."

- "그릇" is clearly a metaphor (vessel/container)
- The target being created is unclear: type? class? data structure? token? field?
- The operation is unclear: definition? allocation? reference?
- Per the rubric: "비유 뒤에 실제 동작이 함께 설명되어 있다면 무조건 지적하지 않는다" - but here, the metaphor IS the entire description; there's no actual operation mentioned
- Verdict: 구체화 필요

Suggested revision: Without more context, we can't know what specific entity is being created. We could say "권한 정보를 보관할 데이터 구조가 필요합니다" or "권한을 표현할 타입이 필요합니다" but these are still vague. The audit should flag the metaphor and ask what the actual entity is.

Actually, the rubric says to suggest revisions. But if we don't know what the entity is, we have to flag it as needing specification. The suggested revision could be a placeholder or a more neutral phrasing.

Let me think about how to format this:

```markdown
## 요약
- 구체화 필요 2건
- 가장 큰 독해 부담: 문장 1의 '그릇'이 실제 대상·동작을 가림

| 위치 | 원문 | 독자가 추측해야 하는 정보 | 판정 | 수정안 | 확인할 사실 |
|---|---|---|---|---|---|
| 1 | 권한을 담아낼 그릇이 필요합니다. | 무엇을 만들려는 대상(타입, 컬렉션, 토큰 등)과 그 정체성(클래스명·구조체명) | 구체화 필요 | "권한 정보를 보관할 데이터 구조가 필요합니다" 등 중립 표현으로 바꾸고, 가능한 경우 실제 식별자 사용 | 이 '그릇'에 해당하는 코드 식별자(타입명·클래스명)는 무엇입니까? |
| 3 | 사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 적용해 거부를 우선합니다. | '거부를 우선'의 적용 범위(어</think>

<think>떤 deny가 어떤 allow를 이기는지)와 '직접'이 사용자 항목에만 붙은 비대칭의 의미 | 구체화 필요 | 우선순위 규칙을 명시적으로 서술. 예: "먼저 사용자 설정을 확인하고, 그다음 역할 설정을 확인한다. 어느 단계에서든 거부가 허용보다 우선한다." | 거부와 허용이 서로 다른 출처일 때(예: 사용자 허용 vs 역할 거부) 어느 쪽이 이기는가? |
```

And then note that sentence 2 passes.

Wait, the user said: "문제가 없는 문장은 별도로 짧게 표시하세요" - sentences without problems should be shown briefly and separately.

So I should:
1. Show sentence 2 as a pass, separately
2. Show sentences 1 and 3 in the table

Let me also think about whether sentence 3's "거부를 우선합니다" really needs revision. Let me re-read the rubric:

The rubric flags:
1. 낯선 결합 (strange combinations)
2. 동작을 대신하는 비유 (metaphors replacing operations)
3. 명사 나열과 과도한 압축 (noun listing and excessive compression)
4. 평가가 사실을 대신함 (evaluation replacing facts)
5. 정보 순서 (information order)
6. 전 영역 검사 (check all areas)

For sentence 3:
- It's mostly a noun phrase listing, but that's appropriate for describing an order
- "거부를 우선합니다" - this is an evaluation/judgment (priority) that could be more specific about the rule
- The asymmetry of "직접" is unclear

I think the main issue is that "거부를 우선합니다" is ambiguous in scope. Is it:
- Within the same source level: deny beats allow?
- Across all sources: any deny beats any allow?

Let me draft the response:

Actually, let me reconsider the format. The skill says:
"When auditing, return a short summary followed by a table with:
`location | source | reader must infer | finding | suggested revision | facts to verify`"

So I should use these exact column headers.

Let me also think: should I flag sentence 3's "직접" asymmetry? The rubric says don't flag just because it's English, figurative, or unfamiliar. The asymmetry here is a stylistic choice that may be intentional. The bigger issue is the ambiguity of "거부를 우선".

Hmm, let me think again. In permission systems like AWS IAM or typical RBAC:
- "사용자 직접 거부" = explicit user deny
- "사용자 직접 허용" = explicit user allow
- "역할 거부" = role deny
- "역할 허용" = role allow

The "직접" might be distinguishing user-set from group-set or inherited. But if roles are also "direct" in some sense, the asymmetry is confusing.

Actually, looking more carefully, the sentence as written might be saying:
- User-set permissions (both deny and allow) take priority
- Role-set permissions come after
- Within this priority, denies always beat allows

The reader must figure this out from the list ordering and "거부를 우선".

I think the main flag is:
- The priority rule needs to be stated explicitly: "어느 단계에서든 거부가 허용보다 우선한다" or similar
- The asymmetry of "직접" might need clarification

Let me finalize:

For sentence 1:
- 위치: 1
- 원문: 권한을 담아낼 그릇이 필요합니다.
- 독자가 추측해야 하는 정보: 대상(데이터 구조, 타입, 컬렉션 등)과 실제 식별자
- 판정: 구체화 필요
- 수정안: 중립적 표현으로 바꾸고 가능한 경우 실제 코드 식별자 사용. 예: "권한 정보를 보관할 타입이 필요하다."
- 확인할 사실: 이 '그릇'에 해당하는 코드 식별자는 무엇인가?

For sentence 3:
- 위치: 3
- 원문: 사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 적용해 거부를 우선합니다.
- 독자가 추측해야 하는 정보: '거부를 우선'의 적용 범위(동일 출처 내인가, 모든 출처 간인가)와 '직접'이 사용자 항목에만 붙은 이유
- 판정: 구체화 필요
- 수정안: 우선순위 규칙을 명시적으로 서술. 예: "먼저 사용자 설정을 확인하고 그다음 역할 설정을 확인한다. 같은 단계에서 거부는 허용보다 우선하며, 거부 결과가 한 번 확정되면 그 뒤 단계를 확인하지 않는다." (단, 실제 규칙에 맞게 조정 필요)
- 확인할 사실: 사용자 허용 vs 역할 거부처럼 출처가 다를 때 어느 쪽이 이기는가?

Hmm, but for sentence 3, I added specific behavior ("확정되면 그 뒤 단계를 확인하지 않는다") that isn't in the source. The semantic fidelity rule says "원문에서 확인할 수 없는 정보를 자연스럽게 보이게 만들기 위해 추가하지 않는다."

So I should mark this as something to verify rather than asserting it in the suggested revision. Let me revise:

수정안: 우선순위 규칙을 명시적으로 서술. 예: "먼저 사용자 설정을 확인하고, 그다음 역할 설정을 확인한다. 어느 단계에서든 거부는 허용보다 우선한다."

확인할 사실: 사용자 허용과 역할 거부처럼 출처가 다른 경우, 거부가 항상 이기는가? 그리고 평가가 단락되는지(deny 확정 시 이후 단계 평가 생략)도 확인 필요.

Better.

Let me also consider if sentence 2 truly passes. Re-reading:
"임시 권한은 만료 시각을 저장하고 각 요청에서 현재 시각과 비교해 유효성을 확인합니다."

- Subject: 임시 권한 (the thing that stores)
- Operation 1: 만료 시각을 저장 (stores expiration time)
- Operation 2: 현재 시각과 비교 (compares with current time)
- Operation 3: 유효성을 확인 (verifies validity)
- Condition: 각 요청에서 (at each request)

The "유효성" - validity of what? Of the temporary permission itself. This is implied but clear from context.

I think this passes.

One more thought: the user asked for the "기본 출력 형식" (default output format), which I interpret as the audit format with summary + table.

Let me also think about whether the "직접" asymmetry is a flag worth noting. The rubric says not to flag just for being unfamiliar or stylistic, but to flag when the wording causes ambiguous target, actor, operation, condition, result, or scope. The asymmetry here causes ambiguous scope (is "직접" implicit for roles, or are roles inherently "direct"?). 

Actually, I think this is more of a stylistic question that could be raised. But the more critical issue is the "거부를 우선" rule. Let me keep my focus on that.

Alright, let me also think about whether I should mark the whole thing differently. Let me draft a cleaner version:

```markdown
## 요약
- 구체화 필요 2건 (문장 1, 3)
- 가장 큰 독해 부담: 문장 1에서 '그릇'이라는 비유가 실제 대상(타입·자료 구조·식별자)을 가리고 있음. 문장 3에서 '거부를 우선한다'는 규칙이 적용 범위(동일 출처 내 vs 모든 출처 간)에서 모호함.

## 통과
- 문장 2: 대상(임시 권한), 동작(만료 시각 저장·현재 시각 비교·유효성 확인), 조건(각 요청에서)이 모두 명시됨.

| 위치 | 원문 | 독자가 추측해야 하는 정보 | 판정 | 수정안 | 확인할 사실 |
|---|---|---|---|---|---|
| 1 | 권한을 담아낼 그릇이 필요합니다. | 만들고자 하는 대상의 정체성(타입, 클래스, 컬렉션 등)과 실제 식별자 | 구체화 필요 | 중립적 표현으로 바꾸고, 가능하면 실제 식별자 사용. 예: "권한 정보를 보관할 타입을 정의해야 한다." | 이 '그릇'에 해당하는 코드 식별자(타입명·클래스명)는 무엇입니까? |
| 3 | 사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 적용해 거부를 우선합니다. | (a) '거부를 우선'의 적용 범위—동일 출처 내 우선인지, 사용자/역할을 가로지르는 절대 우선인지 (b) '직접'이 사용자 항목에만 붙은 비대칭의 의미 | 구체화 필요 | 평가 순서와 우선 규칙을 분리해 서술. 예: "사용자 설정 → 역할 설정 순으로 평가한다. 어느 단계에서든 거부는 허용보다 우선한다." | (1) 사용자 '허용'과 역할 '거부'가 동시에 적용될 때 어느 쪽이 이기는가? (2) 거부가 확정되면 이후 단계 평가를 생략하는 단락 평가가 적용되는가? |
```

This looks good. Let me make sure I'm following the format from output-formats.ko.md:
- "## 요약" with bullet points
- Table with the specified columns
- "문제가 없는 문장은 열거하지 않는다" - so sentence 2 should be briefly noted but not in the table

The user asked to "문제가 없는 문장은 별도로 짧게 표시하세요" - so I should briefly note sentence 2 separately. I'll add a small "통과" section.

Let me finalize my response. I need to use the thinking block first, then provide the response.

One more consideration: the user wrote "설치된 스킬의 기본 출력 형식과 판정 원칙을 따르세요" - follow the installed skill's default output format and judgment principles. So I should:
1. Use the audit format (summary + table)
2. Apply the rubric's judgment principles (don't flag just because it's English/figurative, flag when information is missing)
3. Use the semantic fidelity principles (preserve subject, direction, condition, scope, certainty)

I think my draft does this. Let me also double-check my findings:

Sentence 1: "권한을 담아낼 그릇이 필요합니다."
- Subject: implied (we/developer)
- Operation: needs to create something
- Target: unclear (a "그릇" for permissions)
- The metaphor "그릇" (vessel/container) is a clear case of "동작을 대신하는 비유" from the rubric
- The rubric says: "비유 뒤에 실제 동작이 함께 설명되어 있다면 무조건 지적하지 않는다" - here, no actual operation is described, only the metaphor
- ✓ Flagged correctly

Sentence 2: "임시 권한은 만료 시각을 저장하고 각 요청에서 현재 시각과 비교해 유효성을 확인합니다."
- Subject: 임시 권한
- Operations: clearly described (저장, 비교, 확인)
- Condition: 각 요청에서
- ✓ Pass

Sentence 3: "사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 적용해 거부를 우선합니다."
- Operations: applying in order with priority
- Subject: implied (the permission system)
- The priority rule "거부를 우선" is ambiguous in scope
- The "직접" asymmetry could be noted
- ✓ Flagged for scope ambiguity

Alright, my analysis is solid. Let me write the final response.

Actually, one more thought on sentence 3. Let me think about whether "거부를 우선" is really ambiguous or if it's clear.

The list is: 사용자 직접 거부 → 사용자 직접 허용 → 역할 거부 → 역할 허용
"적용해 거부를 우선합니다"

Possible readings:
1. "Apply in this order: user deny, user allow, role deny, role allow. (When applying,) prioritize denials." - This could mean denials are evaluated first (which they are, in the list) or that any deny beats any allow.
2. "Apply in this order: ..., and within this order, denials take priority." - Could mean deny is checked first, then allow.

The ambiguity is whether "거부를 우선" is just stating that the order puts denies first, or whether it's adding a separate rule that denies beat allows across all sources.

If I had to pick, I think a typical Korean reader would interpret this as: "denials (regardless of source) beat allows (regardless of source)". But the list ordering is also ambiguous in itself - is it evaluation order (short-circuit) or priority order?

Yes, I think the flag is justified. The rule needs to be more explicit.

Let me also note: "사용자 직접 거부" vs "역할 거부" - this asymmetry. The word "직접" (directly) only appears with user. A reader might wonder if "역할 거부" is also "direct" or if there's a "역할 간접 거부" that could exist. This is a stylistic asymmetry that adds slight confusion.

Should I include this in my flag? The rubric says: "Flag the passage only when the wording causes an omitted or ambiguous target, actor, operation, condition, result, or scope." The asymmetry doesn't cause omission but causes slight ambiguity in scope. I think it's worth mentioning briefly but not as the main finding.

OK, let me finalize. I'll write the response in Korean since the input is in Korean.

Final response structure:
1. Think block (this one)
2. Brief summary in markdown
3. Note about sentence 2 passing
4. Table with findings for sentences 1 and 3

Let me write it now.

Actually, let me reconsider sentence 2 one more time. "임시 권한은 만료 시각을 저장하고 각 요청에서 현재 시각과 비교해 유효성을 확인합니다."

Could "임시 권한" be a code identifier? It could be a type name like TemporaryPermission or TemporaryCredential. If so, per the rubric: "코드의 타입명, 함수명, 제품명, 팀 용어집에 있는 말은 영어라는 이유만으로 지적하지 않는다." So if it's a code name, it should be preserved as is.

But also: "식별자: 코드 이름과 타입의 의미를 일반어로 잘못 바꾸지 않았는가?" - I shouldn't translate it to English or change it. Keep as is.

In my response, I should just note that sentence 2 passes because the target, operations, and conditions are clear. I shouldn't change "임시 권한" to anything.

OK, I'm done thinking. Let me write the response.</think>

## 요약
- 구체화 필요 2건(문장 1, 3), 통과 1건(문장 2)
- 가장 큰 독해 부담: 문장 1에서 '그릇'이라는 비유가 실제 대상(타입·자료 구조·식별자)을 가림. 문장 3에서 '거부를 우선한다'는 규칙이 동일 출처 내 우선인지 출처를 가로지르는 절대 우선인지 구분되지 않음.

## 통과
- **문장 2** `임시 권한은 만료 시각을 저장하고 각 요청에서 현재 시각과 비교해 유효성을 확인합니다.` — 대상(임시 권한), 동작(만료 시각 저장 → 현재 시각 비교 → 유효성 확인), 조건(각 요청에서)이 한 문장 안에서 모두 드러나며 추측이 필요 없음.

| 위치 | 원문 | 독자가 추측해야 하는 정보 | 판정 | 수정안 | 확인할 사실 |
|---|---|---|---|---|---|
| 1 | 권한을 담아낼 그릇이 필요합니다. | 만들고자 하는 대상의 정체성(타입, 클래스, 컬렉션, 토큰, 컬럼 등)과 실제 식별자명 | 구체화 필요 | 비유 대신 대상의 역할과 식별자를 직접 쓴다. 예: `권한 정보를 보관할 타입을 정의해야 한다.` 또는 실제 코드 식별자가 정해져 있다면 `Permission`/`Authorization` 같은 명칭으로 치환. | 이 '그릇'에 해당하는 코드 식별자(타입명·클래스명·필드명)는 무엇입니까? |
| 3 | 사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 적용해 거부를 우선합니다. | (a) '거부를 우선'의 적용 범위 — 동일 출처(사용자 내 / 역할 내)에서만 거부가 이기는지, 아니면 사용자 허용 vs 역할 거부처럼 출처를 가로질러서도 거부가 절대 이기는지 (b) '직접'이 사용자 항목에만 붙어 있는 비대칭의 의미(역할 항목은 간접 거부가 존재하지 않는지) | 구체화 필요 | 평가 순서와 우선 규칙을 분리해 명시한다. 예: `먼저 사용자 설정을 평가하고, 그다음 역할 설정을 평가한다. 어느 단계에서든 거부는 허용보다 우선한다.` '직접' 비대칭은 도메인 의미가 다르다면 양쪽 모두에 일관된 수식어를 적용하거나, 차이를 한 문장으로 설명. | (1) 사용자 '허용'과 역할 '거부'가 동시에 적용되는 경우 어느 쪽이 이기는가? (2) 거부가 확정되면 이후 단계 평가를 생략하는 단락 평가가 적용되는가? (3) 역할 항목에 '직접' 수식이 빠진 것은 의도적 비대칭인가, 단순 누락인가? |
