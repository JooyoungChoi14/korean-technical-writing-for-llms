<think>릇 = container/bowl). The rubric says: "동작을 대신하는 비유" — metaphors for actual operations. But here, "그릇" is used for the data structure itself (something that holds permission data), not replacing an action. It's a metaphor for the type/class itself.
- The question is: what type/class/structure? In code, the actual name or category (e.g., "Permission 객체", "Grant 구조체", "Capability 타입") would be more precise.
- However, "그릇" by itself may not be problematic if the surrounding context defines it. As a standalone sentence, it does require the reader to infer what "그릇" refers to specifically.
- This could fall under "동작을 대신하는 비유" — the metaphor of a "vessel" replaces a concrete type/structure name. The reader must infer what the actual data structure is.

Actually, looking more carefully:
- "그릇이 필요합니다" — the metaphor is used to describe the need for a data structure. The reader must infer: what kind of structure? Is it a class, struct, type, field, parameter? 
- Without context, the reader has to guess whether this is a new class definition, a property on an existing class, a parameter, etc.
- This seems like "구체화 필요" — meaning is determined, but target/operation/condition/result is partially obscured.

**Sentence 2: "임시 권한은 만료 시각을 저장하고 각 요청에서 현재 시각과 비교해 유효성을 확인합니다."**
- Target: 임시 권한 (temporary permission)
- Operation: 만료 시각을 저장, 유효성을 확인
- Method: 현재 시각과 비교
- This sentence is quite clear. Subject (임시 권한), operation (만료 시각 저장, 유효성 확인), method (현재 시각과 비교) are all explicit.
- One potential issue: "만료 시각을 저장" — where does the temporary permission store this? Is it a field? An external cache? But this might be over-analyzing.
- "각 요청에서" — clear scope/condition
- "유효성을 확인" — clear operation, though we might wonder what happens on failure (rejection?), but this might not be required if we're just describing the validation step.
- Actually, this looks pretty solid. The subject, operation, method, and scope are all clear.

Hmm, let me reconsider. "임시 권한" could be a class/type, "만료 시각" is a property/field. This is reasonable Korean technical writing.

I think this sentence passes.

**Sentence 3: "사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 적용해 거부를 우선합니다."**
- Target: 권한 적용 규칙 (permission application rules)
- Operation: 순서대로 적용, 거부 우선
- The order is clear, but there's potential ambiguity:
  - "사용자 직접 거부" vs "사용자 직접 허용" — clear
  - "역할 거부" vs "역할 허용" — clear
  - "순으로 적용" — what does this mean exactly? Higher priority? Override? 
  - The order given is: 거부 > 허용 (within same level: user overrides role, both user-level then role-level)
  - "거부를 우선합니다" — this clarifies that denials take priority
  
Actually, the order listed (사용자 직접 거부 → 사용자 직접 허용 → 역할 거부 → 역할 허용) and "거부를 우선합니다" could be redundant or could conflict. Let me re-read.

Wait, if the order is: 사용자 직접 거부 → 사용자 직접 허용 → 역할 거부 → 역할 허용, and we apply them in this order with "거부를 우선" (denial takes priority), then:
- If a user-direct denial exists, it applies (regardless of subsequent items)
- Otherwise, if a user-direct grant exists, it applies
- Etc.

But "거부를 우선" could also mean: if any denial applies, use it. So even if a user-direct grant exists, if a role-denial applies, the denial wins.

The sentence could be ambiguous about which interpretation is meant. The reader must infer whether "거부를 우선" means:
(a) Earlier denial in the list wins over later items, OR
(b) Any denial at any level wins over any grant at any level

This is a case where the reader has to guess the actual policy.

Also, what does "적용" mean exactly? Override? Combine? Compare?

Possible judgment: "의미 확인 필요" — the natural reading is somewhat ambiguous.

Actually, in standard permission systems (like ABAC/RBAC), the typical interpretation would be: explicit deny overrides everything. So "거부를 우선" most likely means "deny wins regardless of source." But the ordering of the list could also imply sequential evaluation.

This ambiguity is the problem — the sentence can be read two different ways, and the reader must guess the policy.

Let me also consider: 
- "사용자 직접" — what does "직접" mean here? Direct user (as opposed to inherited from group/role)? This might be clear in context.
- The four items in the list — are these the only four? Or are these just examples?

Hmm, this is getting nuanced. Let me think about my judgments:

**Sentence 1: "권한을 담아낼 그릇이 필요합니다."**
- 문제: 그</think>

<think>릇이라는 비유가 실제 타입/구조/필드명을 대신함. 독자는 무엇을 추가해야 하는지(클래스? 필드? 매개변수?) 추측해야 함.
- 판정: 구체화 필요

**Sentence 2: "임시 권한은 만료 시각을 저장하고 각 요청에서 현재 시각과 비교해 유효성을 확인합니다."**
- 문제 없음. 주체(임시 권한), 동작(저장/비교/확인), 조건(각 요청), 결과(유효성)가 명시됨.
- 판정: 통과

**Sentence 3: "사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 적용해 거부를 우선합니다."**
- 문제: "순으로 적용"과 "거부를 우선"의 관계가 모호함. 두 가지 해석이 가능:
  - (a) 위에서부터 순서대로 평가, 처음 매칭되는 것 채택
  - (b) 어떤 단계에서든 거부가 있으면 거부 채택
- 판정: 의미 확인 필요 (or 구체화 필요)

Let me also check: does "사용자 직접 거부" — the "직접" word. In Korean permission systems, "사용자 직접" often means "explicitly set by user/admin" vs "inherited from role/group." This is fine if the context establishes it.

Actually, let me reconsider sentence 1 more carefully. "그릇" might just be a stylistic metaphor for a data container. In technical docs, this could be acceptable if the surrounding code/text defines what the container is. But as a standalone sentence, it's vague.

Looking at the rubric again:
"동작을 대신하는 비유 - 입력·저장·호출·반환·검증·노출 같은 동작을 손잡이, 관문,</think>

<think> 뼈대,</think>

<think> 껍데기 같은 사물이나 이동으로만 설명하는가?"

In sentence 1, "그릇" is a metaphor for the data structure itself, not for an operation. The operation is "필요합니다" (is needed). So this might be a different issue.

But the rubric also says: "비유 뒤에 실제 동작이 함께 설명되어 있다면 무조건 지적하지 않는다."

In sentence 1, the "그</think>

<think>릇" is being introduced as a concept that needs to be defined. The reader needs to know what this container is called in the code, what type it has, what fields it holds.

Actually, I think the issue here is more about "구체화 필요" — the target is vague (그</think>

<think>릇 instead of a specific class/struct/type name). The operation "필요합니다" is clear.

Hmm, but "그릇" is a common metaphor in Korean for a data container. Let me think again.

In technical writing, "그</think>

<think>릇" alone is too vague. The reader must infer:
- What is being created? A class? A struct? A property?
- What is its name in code?
- What does it actually contain?

So this is a "구체화 필요" case.

Let me also consider sentence 3 more carefully:

"사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 적용해 거부를 우선합니다."

Re-reading this, I think there's another potential issue: 
- "역할 거부" and "역할 허용" — does "역할" here mean "role" (RBAC sense) or "function"? In Korean tech context, 역할 usually means role.
- "사용자 직접" — what's the contrast? Implicit "역할을 통한" (through role)?

But these are likely fine if the surrounding text defines them.

The main issue I see is the ambiguity in "순으로 적용" + "거부를 우선":
- Reading 1: 위에서부터 순차 평가, 첫 번째 매치 채택 (top-down, first match wins)
  - 사용자 직접 거부 있으면 적용
  - 없으면 사용자 직접 허용 적용
  - 없으면 역할 거부 적용
  - 없으면 역할 허용 적용
- Reading 2: 거부 > 허용 우선 원칙 + 같은 차원 내 순서
  - 어떤 거부든 있으면 거부
  - 같은 차원에서는 사용자 > 역할

These two readings give different results when, e.g., 사용자 직접 허용 + 역할 거부 are both set. Reading 1 would say 허용 (since 거부 isn't in user's list), Reading 2 would say 거부.

So the reader must guess which policy is intended.

This is a "의미 확인 필요" case because the natural reading is ambiguous and we can't determine the intended policy from the source alone.

OK let me draft the response.

Actually, looking at the output format again:
"문제가 없는 문장은 열거하지 않는다. 지적의 근거는 취향이 아니라 누락되거나 모호한 정보로 쓴다."

And: "세 문장을 모두 검토하되, 문제가 없는 문장은 별도로 짧게 표시하세요."

So I should:
1. Audit the sentences (only flag problematic ones)
2. Show passing sentences briefly

Let me structure my response:

## 요약
- 구체화 필요 1건, 의미 확인 필요 1건
- 가장 큰 독해 부담: 대상을 가리는 비유와 정책 우선순위 해석의 모호성

## 문제 문장
[table for sentence 1 and 3]

## 통과 문장
- 2번: ...

Let me now write this out properly.

Actually, let me reconsider sentence 2 one more time:
"임시 권한은 만료 시각을 저장하고 각 요청에서 현재 시각과 비교해 유효성을 확인합니다."

- 임시 권한 (subject): 임시 권한 grants/credentials that have an expiration
- 만료 시각을 저장 (operation 1): stores expiration timestamp
- 각 요청에서 (scope): per request
- 현재 시각과 비교해 (method): compare with current time
- 유효성을 확인합니다 (operation 2): checks validity

I think this is clear. The reader doesn't need to guess. Pass.

Wait, one minor thing: "유효성을 확인" — what happens when invalid? Reject the request? But this might not be in scope for describing the validation step. I'll let it pass.

Now let me also reconsider whether sentence 1's "그릇" might be acceptable. In Korean tech writing, "그</think>

<think>릇" can be a common metaphor for data structure. But:
- The rubric says: "동작을 대신하는 비유 - ... 손잡이, 관문, 뼈대, 껍데기 같은 사물"
- "그릇" is a 사물 metaphor, but it's used for the data structure itself, not for an operation
- However, the broader principle is: "비유 뒤에 실제 동작이 함께 설명되어 있다면 무조건 지적하지 않는다."
- In sentence 1, the issue isn't a missing operation; the operation is "필요합니다" (we need to create one). The issue is that the target itself is a metaphor.

So I'd say this is "구체화 필요" — the target is hidden behind a metaphor, so the reader can't tell what specifically needs to be added.

Alternatively, I could argue this is "의미 확인 필요" if we genuinely don't know what type of structure is intended.

Hmm, let me re-read the rubric:
- "구체화 필요": 뜻은 확정할 수 있으나 대상·동작·조건·결과 일부가 표현에 가려졌다.
- "의미 확인 필요": 자연스럽게 고칠 수는 있지만 원문만으로 정확한 뜻을 확정할 수 없다.

For sentence 1, I think the meaning is somewhat determinable (we need a container/structure for permission), but the specific target (what kind of structure, what name) is obscured. So it's "구체화 필요."

For sentence 3, the policy interpretation can't be determined from the source alone. So it's "의미 확인 필요."

Let me also think: should I use the table format with location | source | reader must infer | finding | suggested revision | facts to verify? Yes.

Final structure:

## 요약
- 구체화 필요 1건 (1번), 의미 확인 필요 1건 (3번)
- 가장 큰 독해 부담: 비유가 대상 자체를 가리는 경우(1번), 우선순위와 순차 평가가 함께 쓰여 정책이 모호해지는 경우(3번)

## 통과 문장
- 2번: 주체(임시 권한), 동작(저장·비교·확인), 조건(각 요청)이 모두 명시되어 문장 자체로 의미가 완결됨.

## 문제 문장

### 1번

| 위치 | 원문 | 독자가 추측해야 하는 정보 | 판정 | 수정안 | 확인할 사실 |
|---|---|---|---|---|---|
| 본문 1 | "권한을 담아낼 그릇이 필요합니다." | "그릇"이 가리키는 실제 대상(클래스/구조체/필드/매개변수 등)과 그 이름 | 구체화 필요 | "권한 정보를 담을 Permission 타입(또는 구체 명칭) 클래스를 추가한다." 등 | 도입하려는 데이터 구조의 코드상 이름과 종류 |

### 3번

| 위치 | 원문 | 독자가 추측해야 하는 정보 | 판정 | 수정안 | 확인할 사실 |
|---|---|---|---|---|---|
| 본문 3 | "사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 적용해 거부를 우선합니다." | "순으로 적용"이 (a) 순차 평가 후 첫 매치 채택인지, (b) "거부를 우선"과 결합한 우선순위 규칙인지 | 의미 확인 필요 | 우선 적용할 항목을 더 명시적으로 표현, 예: "허용 결정은 사용자 직접 → 역할 순으로 평가하고, 어느 단계에서든 거부가 있으면 그 결과를 채택한다." | 우선 적용 정책이 '순차 평가'인지 '거부 절대 우선'인지, 그리고 사용자/역할 차원의 우선 비교 방식 |

Hmm, let me think about the suggestions more carefully.

For sentence 1, the suggestion should preserve the meaning that we need a container for permissions, but specify what kind. I shouldn't invent a specific type name. Let me adjust:

"권한 정보를 보관할 데이터 구조(예: PermissionInfo 구조체 또는 권한 객체)를 도입한다."

Actually, the instruction says: "원문에서 확인할 수 없는 구현체·자료 구조·정책을 수정안에 사실처럼 추가하지 말고, 필요한 최소 확인 질문을 남기세요."

So I should not invent a specific struct name like "PermissionInfo". Instead, I should keep it general and ask for verification.

Let me revise:
"권한 정보를 담을 데이터 구조가 필요하다."
But this still uses "데이터 구조" which is more specific than "그릇" but not making things up.

Actually, the suggestion should make the target clear. If we don't know what specific type to introduce, we should describe the functional role:
"권한과 그 만료 시각을 함께 보관하는 구조(클래스, 구조체 등 코드상 명칭 미정)를 추가한다."

This is more concrete without inventing a specific name.

For sentence 3, I should clarify the priority rules without assuming a specific implementation:
"사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 평가하되, 어느 단계에서든 거부가 나오면 그 결과를 채택한다."
or
"거부 결정은 허용 결정보다 우선한다. 사용자 차원과 역할 차원이 동시에 비거부일 때는 사용자 직접 결정을 채택한다."

I think the second version is clearer if that's the intended policy.

But since I'm not sure of the intended policy, I'll suggest a clearer phrasing and ask for verification.

Let me also think: is the second sentence really passing? Let me read once more.

"임시 권한은 만료 시각을 저장하고 각 요청에서 현재 시각과 비교해 유효성을 확인합니다."

- 임시 권한 (subject): what kind of temporary permission? Bearer token? Session token? API key? But this might be defined elsewhere.
- 만료 시각을 저장: stores expiration time — clear
- 각 요청에서: per request — clear scope
- 현재 시각과 비교해: compare with current time — clear method
- 유효성을 확인합니다: checks validity — clear result

I think this is fine. Pass.

OK, let me draft the final response.

Actually, one more consideration for sentence 1: "그릇" metaphor. The rubric example was "상태를 화면으로 꺼낼 구멍을 연다" which is about an operation (open a hole for state to come out to the screen). The suggested revision was "화면이 상태를 읽을 수 있도록 status 속성을 공개한다" which replaces the metaphor (구</think>

<think>멍/</think>

<think>꺼내다) with the actual API operation (status 속성 공개).

Similarly, sentence 1 uses "그릇" as a metaphor for the data structure. The actual operation is "create/define a container class/type." But here the metaphor is the target, not the operation.

Looking at the rubric again:
"동작을 대신하는 비유 - 입력·저장·호출·반환·검증·노출 같은 동작을 손잡이, 관문, 뼈대, 껍데기 같은 사물이나 이동으로만 설명하는가?"

Hmm, "뼈대, 껍데기" are listed as examples of 비유 that describe something structural. "그릇" is similar — it's a physical object metaphor for a data container.

The example in the rubric for "동작을 대신하는 비유" is about an action (opening a hole), not about a noun. But the principle could extend to cases where a metaphor replaces a concrete technical term.

Let me reframe: the issue with sentence 1 is that "그릇" is a metaphor for the actual data type/structure. The reader needs to know what to call it in the code, what fields it has, etc.

Judgment: 구체화 필요 (target/condition/result partially obscured by metaphor)

Suggestion: keep "그릇" if needed but clarify what it represents:
- "권한과 만료 시각을 함께 보관할 자료 구조를 도입한다."
- Or if the document discusses a specific class name: use that name.

Actually, the example in the rubric "상태를 화면으로 꺼낼 구멍을 연다" → "status 속성을 공개한다" shows that the revision should use the actual technical term (속성 = attribute/property) rather than the metaphor (구멍 = hole).

So for sentence 1, the revision should use the actual technical term (e.g., "권한 보관 구조" or "권한 객체") instead of "그릇."

Let me finalize my response.

I'll structure it as:

## 요약
- 구체화 필요 1건 (1번), 의미 확인 필요 1건 (3번)
- 가장 큰 독해 부담: 비유(그</think>

<think>릇)가 대상 자체를 가리는 경우, 우선순위와 순차 평가 표현이 겹쳐 정책 해석이 갈리는 경우

## 통과 문장
- 2번: 주체(임시 권한)·동작(저장·비교·확인)·조건(각 요청)이 모두 드러나 문장 자체로 의미가 완결됨.

## 문제 문장

### 1번

| 위치 | 원문 | 독자가 추측해야 하는 정보 | 판정 | 수정안 | 확인할 사실 |
|---|---|---|---|---|---|
| 본문 | "권한을 담아낼 그릇이 필요합니다." | 도입할 대상의 종류(클래스/구조체/필드 등)와 코드상 명칭 | 구체화 필요 | "권한과 만료 시각을 함께 보관할 자료 구조(예: Permission 같은 권한 객체)를 추가한다." | 이 문서가 다루는 자료 구조의 실제 이름과 종류 |

### 3번

| 위치 | 원문 | 독자가 추측해야 하는 정보 | 판정 | 수정안 | 확인할 사실 |
|---|---|---|---|---|---|
| 본문 | "사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 적용해 거부를 우선합니다." | "순으로 적용"이 (a) 위에서부터 순차 평가해 첫 매치를 채택하는지, (b) "거부 우선" 원칙과 결합한 우선순위 규칙인지 | 의미 확인 필요 | "거부 결정이 허용 결정보다 항상 우선하며, 사용자 차원과 역할 차원이 모두 비거부일 때는 사용자 결정을, 둘 다 없을 때는 역할 결정을 채택한다." | 우선 적용 정책이 '순차 평가'인지 '거부 절대 우선'인지, 그리고 사용자/역할 차원의 우선 비교 방식 |

Hmm, I should also check: the suggestion for sentence 3 should not invent policies. Let me think... my suggested revision does include specific policy details ("사용자 차원과 역할 차원이 모두 비거부일 때는 사용자 결정을, 둘 다 없을 때는 역할 결정을 채택한다"), but these are reasonable inferences from the order given in the original.

Actually, looking at the original order: 사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용. If we interpret this as top-down priority (matching the first rule that fires), then:
- If user-direct deny: use it
- Else if user-direct grant: use it
- Else if role deny: use it
- Else if role grant: use it
- Else: no permission?

But "거부를 우선" suggests a global rule: deny wins over grant. Under this interpretation:
- If any deny at any level: deny
- Else if any grant at any level: grant
- The ordering of grants (user-direct vs role) is only relevant if both grant and no deny.

These two interpretations are different.

For my suggested revision, I should pick the most likely interpretation OR explicitly note the ambiguity. Let me restructure:

The revision I wrote assumes the policy is "deny always wins, then user-direct over role." This is a common permission system pattern. But I should mark this as needing verification.

Actually, I think the suggested revision is fine as long as I clearly mark it as one possible interpretation and ask for verification of the policy. The "확인할 사실" column does this.

OK let me also reconsider sentence 1 once more. The metaphor "그릇" is being used to introduce a new data structure. The issue is the reader doesn't know what code-level entity to create. But actually, maybe "그릇" here is fine if the document is at a high level of abstraction (e.g., "we need a container for permissions" as an architectural decision). In that case, the actual class/struct would be defined later in the document.

But the rubric says: "비유 뒤에 실제 동작이 함께 설명되어 있다면 무조건 지적하지 않는다." Sentence 1 doesn't have a real operation described — the operation is "필요합니다" (need), which is a statement of requirement, not a description of what the structure does.

I think the issue here is that without knowing the actual class/struct, the reader can't proceed to implement it. The "그릇" metaphor is too vague.

OK, my judgment stands: 구체화 필요.

Let me also think about whether I should flag anything else in sentence 1 or sentence 3.

Sentence 1:
- "권한을 담아낼" — "담아낼" is a metaphor (contain, hold). This verb is somewhat figurative but commonly used in Korean to mean "store/contain." Combined with "그릇," it's a layered metaphor. I think flagging "그릇" is enough.

Sentence 3:
- "사용자 직접" — the "직접" (direct) word. This implies indirect (i.e., through group/role inheritance). Clear enough in context.
- "순으로 적용" — ambiguous as discussed.
- "거부를 우선" — could be interpreted as a separate principle or as a clarification of the order.
- "사용자" vs "역할" — clear enough.

I'll stick with one issue per sentence as flagged.

Actually, I realize I should double-check sentence 2 one more time. The original is:
"임시 권한은 만료 시각을 저장하고 각 요청에서 현재 시각과 비교해 유효성을 확인합니다."

Let me parse:
- 주어: 임시 권한
- 술어 1: 만료 시각을 저장하고
- 조건: 각 요청에서
- 방법: 현재 시각과 비교해
- 술어 2: 유효성을 확인합니다

All elements are present and clear. Pass.

OK now let me write the final response.

Wait, one more thing. The user said "문제가 없는 문장은 별도로 짧게 표시하세요" — sentences without problems should be displayed briefly and separately. Let me make sure I do this.

Let me also reconsider if "임시 권한" needs more specification. Could it be:
- A type of permission object (e.g., temporary grants)
- A role/attribute (e.g., temporary role)
- A credential (e.g., session token)

But in context, "임시 권한" is likely a well-defined term in the project. Without seeing the broader context, I'll trust that it's clear.

Final draft:

## 요약
- 구체화 필요 1건 (1번), 의미 확인 필요 1건 (3번)
- 가장 큰 독해 부담: 비유(그릇)가 도입 대상 자체를 가려 무엇을 만들어야 할지 확정되지 않는 점(1번), '순으로 적용'과 '거부를 우선'이 함께 쓰여 우선순위 정책이 두 가지로 읽히는 점(3번)

## 통과
- **2번**: 주체(임시 권한)·동작(저장·비교·확인)·조건(각 요청)·결과(유효성)가 모두 명시되어 문장 자체로 의미가 완결됨.

## 문제

| 위치 | 원문 | 독자가 추측해야 하는 정보 | 판정 | 수정안 | 확인할 사실 |
|---|---|---|---|---|---|
| 1번 | "권한을 담아낼 그릇이 필요합니다." | "그릇"이 가리키는 실제 자료 구조의 종류(클래스/구조체/필드/매개변수 등)와 코드상 명칭 | 구체화 필요 | "권한 정보와 만료 시각을 함께 보관할 자료 구조(예: Permission 객체)를 도입한다." | 이 문서가 정의하는 자료 구조의 실제 이름과 종류 |
| 3번 | "사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 적용해 거부를 우선합니다." | "순으로 적용"이 (a) 위에서부터 순차 평가해 첫 매치를 채택하는지, (b) "거부 우선"이 별도의 절대 원칙인지 — 같은 입력에 대해 두 결과가 갈릴 수 있어 확정 불가 | 의미 확인 필요 | "거부 결정은 어느 단계에서든 허용 결정보다 우선한다. 비거부 결정끼리는 사용자 직접 → 역할 순으로 평가해 첫 매치를 채택한다." 또는 "위 순서대로 평가해 첫 번째로 매치되는 결정을 채택하되, 동일한 우선순위에서 거부는 허용을 이긴다."처럼 우선원칙을 한 문장으로 명시 | 우선 적용 정책이 '순차 평가'인지 '거부 절대 우선'인지, 그리고 사용자/역할 차원의 비교 방식 |

I think this is good. Let me also add a brief note about how I evaluated sentence 2 since it passes.

Actually, looking at the format guide:
"문제가 없는 문장은 열거하지 않는다. 지적의 근거는 취향이 아니라 누락되거나 모호한 정보로 쓴다."

But the user explicitly asked: "문제가 없는 문장은 별도로 짧게 표시하세요." So I should follow the user's instruction and briefly display it.

Let me also self-check per the output-formats instructions:
1. Same sentence shouldn't be passing in summary and problematic in table — consistent here.
2. Don't add unsupported implementation details — my suggestions use generic terms like "자료 구조" and "Permission 객체" with "(예: ...)" to indicate they're illustrative, not invented facts.
3. Multiple rule conflicts — sentence 3 has both "순으로 적용" and "거부를 우선" which can be read together or as separate rules. I noted this as the issue.

Let me finalize the response.

One more refinement: the suggestion for sentence 1 says "Permission 객체" which might be too specific. Let me use a more generic phrasing:

"권한 정보와 만료 시각을 함께 보관할 자료 구조를 도입한다." (without the parenthetical example)

Or keep the example but mark it clearly as illustrative:
"권한 정보와 만료 시각을 함께 보관할 자료 구조(예시 명칭: Permission 객체 등, 코드상 실제 이름 확인 필요)를 도입한다."

Actually, I think keeping it simple and generic is better. Let me say:
"권한과 만료 시각을 함께 보관할 자료 구조를 도입한다."

And note in "확인할 사실" that the actual code name needs to be confirmed.

Final response coming up.

Hmm actually for sentence 3, the two possible interpretations I identified:
(a) Top-down sequential evaluation with first match wins
(b) Global rule: deny wins, then user-direct over role

These are quite different. Let me make sure my suggested revisions correspond to each interpretation:

For interpretation (a):
"위 순서대로 평가해 첫 번째로 매치되는 결정을 채택한다."

For interpretation (b):
"거부 결정은 어느 단계에서든 허용 결정보다 우선한다. 사용자 직접과 역할 결정이 모두 허용이거나 모두 비거부일 때 사용자 결정을 채택한다."

I should provide both or ask which one is intended.

Let me write:
"[확인 필요] 우선 적용 정책이 다음 중 어느 쪽인지 확인 필요.
- (a) 위 순서대로 평가해 첫 번째 매치 채택
- (b) 거부 절대 우선 + 사용자/역할 내 사용자 우선"

This matches the rubric's "[확인 필요]" pattern.

OK, final response:

Actually let me re-read sentence 3 once more to make sure I'm interpreting it correctly:

"사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 적용해 거부를 우선합니다."

Word by word:
- 사용자 직접 거부: user direct deny
- 사용자 직접 허용: user direct allow
- 역할 거부: role deny
- 역할 허용: role allow
- 순으로: in order
- 적용해: apply
- 거부를 우선합니다: prioritize deny

Yes, my analysis is correct. The ambiguity I identified is real.

Alright, writing the final response now.

For sentence 3, my suggestion should be more concrete but still acknowledge the ambiguity. Let me try:

If policy is (a) sequential:
"사용자 직접 거부 → 사용자 직접 허용 → 역할 거부 → 역할 허용 순으로 평가해, 가장 먼저 매치되는 결정을 적용한다."

If policy is (b) deny-priority:
"거부 결정은 허용 결정보다 우선한다. 사용자 직접과 역할 결정이 모두 거부이거나 모두 비거부일 때는 사용자 결정을 채택한다."

I'll suggest both and ask for clarification.

Let me write this out in a clean format.

Also for sentence 1, let me reconsider: "권한을 담아낼 그릇이 필요합니다."

If we interpret "그릇" as a data structure, the more natural Korean technical writing would be:
"권한을 보관할 데이터 구조가 필요하다." or "권한 정보를 저장할 자료 구조를 도입한다."

But if we don't know the specific structure, we should:
1. Not invent a specific name
2. Indicate what the structure should hold

Suggestion: "권한 정보(와 필요 시 만료 시각)를 보관할 자료 구조를 도입한다."

This is generic but specifies the contents.

OK final final response time.

Actually, one more consideration. Sentence 1 says "필요합니다" (is needed). This is a requirement statement, not an action. So the "그</think>

<think>릇" is the requirement's target.

In a design doc, you might say "we need a container for permissions." That's fine as a high-level statement. But "그릇" alone is too vague — it doesn't tell us what kind of structure.

My judgment remains: 구체화 필요.

Let me finalize.

Actually, looking at sentence 1 again: "권한을 담아낼 그릇이 필요합니다." — "그릇" might also be interpreted as a UI container (like a permissions dialog box). In design docs, this could be either backend data structure or UI component. Without more context, we can't tell.

So this is actually borderline "의미 확인 필요" rather than "구체화 필요":
- If we're sure it's a data structure but not the specific name: 구체화 필요
- If we're not sure if it's data, UI, or something else: 의미 확인 필요

I'll lean toward "구체화 필요" but acknowledge the scope uncertainty in the "확인할 사실" column.

OK truly final response now.

One more thought on sentence 3. Let me reconsider whether the ambiguity I identified is real.

"사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 적용해 거부를 우선합니다."

Reading 1: 순차 평가
- If user-direct deny exists → deny
- Else if user-direct allow exists → allow
- Else if role-deny exists → deny
- Else if role-allow exists → allow
- Else → no permission (or default)

Reading 2: 거부 우선 + 사용자 > 역할
- If any deny exists (user-direct or role) → deny
- Else if user-direct allow → allow
- Else if role-allow → allow

These two readings give different results when:
- user-direct allow exists AND role-deny exists
- Reading 1: allow
- Reading 2: deny

So yes, the ambiguity is real and policy-affecting. 의미 확인 필요 is appropriate.

OK now writing the response.

Let me also think about whether I should suggest specific Korean phrasing or just point out the issue. Per the rubric: "수정안" column should suggest a revision.

For sentence 1, my revision should:
- Replace "그릇" with something more concrete
- Not invent a specific code name

"권한 정보와 만료 시각을 함께 보관할 자료 구조를 도입한다."

Or keeping "그</think>

<think>릇" but adding details:
"권한(과 필요 시 만료 시각)을 담아낼 자료 구조가 필요하다. 이 구조는 코드상에서 [확인 필요: 실제 이름]이라고 부른다."

Hmm, that's awkward. Let me try:
"권한과 만료 시각을 보관할 자료 구조가 필요하다. 자료 구조의 구체적인 이름과 종류(클래스/구조체 등)는 별도로 확정한다."

This separates the requirement from the naming decision.

Actually, in a typical audit response, the suggestion should be more concise. Let me use:
"권한과 만료 시각을 보관할 자료 구조를 도입한다."

And note the verification question separately.

For sentence 3, my revision depends on which policy is intended. I'll provide both interpretations:
- "(a) 순차 평가로 해석: '위 순서대로 평가해 첫 번째로 매치되는 결정을 적용한다.'"
- "(b) 거부 우선 원칙으로 해석: '거부 결정은 허용 결정보다 항상 우선하며, 사용자 직접과 역할이 모두 비거부일 때는 사용자 결정을 채택한다.'"

And ask which one matches the actual policy.

OK truly writing the response now. Final version:

```markdown
## 요약
- 구체화 필요 1건(1번), 의미 확인 필요 1건(3번)
- 가장 큰 독해 부담: 비유(그릇)가 도입 대상 자체를 가려 무엇을 만들어야 할지 확정되지 않는 점(1번), '순으로 적용'과 '거부를 우선'이 함께 쓰여 같은 입력에 대해 두 가지 다른 우선순위 정책으로 읽히는 점(3번)

## 통과
- **2번**: 주체(임시 권한)·동작(저장·비교·확인)·조건(각 요청)이 모두 드러나 문장 자체로 의미가 완결됨. '무엇을' 어디에 '어떻게' 비교해 '어떤 결과를' 내는지 추정 없이 읽힘.

## 문제

| 위치 | 원문 | 독자가 추측해야 하는 정보 | 판정 | 수정안 | 확인할 사실 |
|---|---|---|---|---|---|
| 1번 | "권한을 담아낼 그릇이 필요합니다." | '그릇'이 가리키는 대상의 종류(클래스/구조체/필드/매개변수/UI 컨테이너 등)와 코드상 이름 | 구체화 필요 | "권한과 만료 시각을 함께 보관할 자료 구조를 도입한다." | 이 문서가 다루는 자료 구조의 실제 종류와 코드상 명칭(그리고 만료 시각 보관 여부) |
| 3번 | "사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 적용해 거부를 우선합니다." | '순으로 적용'이 (a) 위에서부터 순차 평가해 첫 매치를 채택하는지, (b) '거부 우선'이 별도의 절대 원칙인지 — 두 해석은 사용자 직접 허용 + 역할 거부 케이스에서 결과가 갈림 | 의미 확인 필요 | "거부 결정은 어느 단계에서든 허용 결정보다 우선한다. 사용자 차원과 역할 차원이 모두 비거부일 때는 사용자 직접 결정을 채택한다." (b 해석 예시) | 우선 적용 정책이 '순차 평가'인지 '거부 절대 우선'인지, 그리고 사용자/역할 차원의 비교 방식 |

## 의미 확인 필요 (별도 정리)
- 3번: 우선 적용 정책의 정확한 형태. 사용자 직접 허용과 역할 부거부가 동시에 있는 경우 어떤 결과가 나와야 하는지가 확정되지 않음.
```

Actually, the last section overlaps with the table. Let me remove it since the table already has this info.

Hmm, the rubric format says "수정안" should suggest a revision. But for sentence 3, since the policy isn't clear, I should acknowledge that. Let me revise to provide both possible phrasings:

Actually the cleaner approach: provide one phrasings as the most likely (deny-priority) since "거부를 우선" suggests this strongly, but note that the user-direct vs role ordering needs to be clarified.

Or: just describe what needs to be specified and ask for verification, without committing to a specific revision.

Let me try: "거부 결정은 허용 결정보다 우선한다. 사용자/역할 차원 간 우선 비교 방식과 순차 평가 여부를 별도로 명시한다." — this is too vague.

Better: just present the two options in the "확인할 사실" column and let the user decide.

Let me revise the suggestion: "다음 두 가지 중 의도에 맞는 쪽으로 분리해 적는다.
- 순차 평가 해석: '위 순서대로 평가해 첫 번째로 매치되는 결정을 적용한다.'
- 거부 절대 우선 해석: '거부 결정은 허용 결정보다 항상 우선하며, 사용자 직접과 역할이 모두 비거부일 때는 사용자 결정을 채택한다.'"

OK final version. Let me put it together.

Actually I think providing both is good practice. Let me commit to this format.

Let me also double-check the format requirements. The output-formats.md says:

```markdown
## 요약
- 구체화 필요 N건, 의미 확인 필요 N건
- 가장 큰 독해 부담: …

| 위치 | 원문 | 독자가 추측해야 하는 정보 | 판정 | 수정안 | 확인할 사실 |
|---|---|---|---|---|---|
```

OK matches my format.

And the user asked: "세 문장을 모두 검토하되, 문제가 없는 문장은 별도로 짧게 표시하세요."

So I should briefly show passing sentences. I'll add a "통과" section.

Alright, final response:

```markdown
## 요약
- 구체화 필요 1건(1번), 의미 확인 필요 1건(3번)
- 가장 큰 독해 부담: 비유(그릇)가 도입 대상 자체를 가려 무엇을 만들어야 할지 확정되지 않는 점(1번), '순으로 적용'과 '거부를 우선'이 함께 쓰여 같은 입력에 대해 두 가지 다른 우선순위 정책으로 읽히는 점(3번)

## 통과
- **2번**: 주체(임시 권한)·동작(저장·비교·확인)·조건(각 요청)·결과(유효성 확인)가 모두 드러나 문장 자체로 의미가 완결됨.

## 문제

| 위치 | 원문 | 독자가 추측해야 하는 정보 | 판정 | 수정안 | 확인할 사실 |
|---|---|---|---|---|---|
| 본문 1번 | "권한을 담아낼 그릇이 필요합니다." | '그릇'이 가리키는 대상의 종류(클래스/구조체/필드/매개변수 등)와 코드상 이름, 만료 시각 보관 여부 | 구체화 필요 | "권한 정보(와 필요 시 만료 시각)를 보관할 자료 구조를 도입한다." | 이 문서가 다루는 자료 구조의 실제 종류와 코드상 명칭, 만료 시각 보관 여부 |
| 본문 3번 | "사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 적용해 거부를 우선합니다." | '순으로 적용'이 (a) 위에서부터 순차 평가해 첫 매치를 채택하는지, (b) '거부 우선'이 별도의 절대 원칙인지 — 두 해석은 사용자 직접 허용 + 역할 거부 케이스에서 결과가 갈림 | 의미 확인 필요 | 다음 중 의도에 맞는 쪽으로 명시한다. (a) 순차 평가: "위 순서대로 평가해 첫 번째로 매치되는 결정을 적용한다." (b) 거부 절대 우선: "거부 결정은 허용 결정보다 항상 우선하며, 사용자 직접과 역할이 모두 비거부일 때는 사용자 직접 결정을 채택한다." | 우선 적용 정책이 '순차 평가'인지 '거부 절대 우선'인지, 그리고 사용자/역할 차원의 비교 방식(특히 사용자 직접 허용과 역할 부거부가 동시에 있는 경우) |
```

This looks good. Let me also do a final self-check per output-formats:
1. Consistent judgments — yes, passing only 2, problematic 1 and 3.
2. No invented facts — yes, I use generic terms and ask for verification.
3. Multiple rule conflicts — sentence 3 has '순으로 적용' and '거부를 우선' which conflict in some cases. I've identified this as the issue.

OK submitting this.## 요</think>

약
- 구체화 필요 1건(1번), 의미 확인 필요 1건(3번)
- 가장 큰 독해 부담: 비유("그릇")가 도입 대상 자체를 가려 무엇을 만들어야 할지 확정되지 않는 점(1번), '순으로 적용'과 '거부를 우선'이 함께 쓰여 같은 입력에 대해 두 가지 다른 우선순위 정책으로 읽히는 점(3번)

## 통과
- **2번**: 주체(임시 권한)·동작(저장·비교·확인)·조건(각 요청)·결과(유효성 확인)가 모두 드러나 문장 자체로 의미가 완결됨. 만료 시각이 어디에 보관되고, 언제 어떤 값과 비교되며, 무엇을 반환하는지가 추정 없이 읽힘.

## 문제

| 위치 | 원문 | 독자가 추측해야 하는 정보 | 판정 | 수정안 | 확인할 사실 |
|---|---|---|---|---|---|
| 본문 1번 | "권한을 담아낼 그릇이 필요합니다." | "그릇"이 가리키는 대상의 종류(클래스/구조체/필드/매개변수 등)와 코드상 이름, 그리고 만료 시각 보관 여부 | 구체화 필요 | "권한 정보(와 필요 시 만료 시각)를 보관할 자료 구조를 도입한다." | 이 문서가 다루는 자료 구조의 실제 종류와 코드상 명칭, 그리고 만료 시각을 같은 자료 구조에 함께 보관하는지 별도 컬렉션에 두는지 |
| 본문 3번 | "사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 적용해 거부를 우선합니다." | "순으로 적용"이 (a) 위에서부터 순차 평가해 첫 매치를 채택하는지, (b) "거부를 우선"이 별도의 절대 원칙인지 — 두 해석은 사용자 직접 허용 + 역할 거부가 동시에 있는 경우 결과가 갈림 | 의미 확인 필요 | 의도에 맞는 쪽을 골라 명시한다.<br>(a) 순차 평가: "위 순서대로 평가해 첫 번째로 매치되는 결정을 적용한다."<br>(b) 거부 절대 우선: "거부 결정은 허용 결정보다 항상 우선하며, 사용자 직접과 역할이 모두 비거부일 때만 사용자 직접 결정을 채택한다." | 우선 적용 정책이 '순차 평가'인지 '거부 절대 우선'인지, 그리고 사용자/역할 차원의 비교 방식(특히 사용자 직접 허용과 역할 부거부가 동시에 존재하는 케이스의 기대 결과) |
