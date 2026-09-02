<think>릇이 필요 (need a container to hold them)
- The metaphor "그릇" (container/dish) is being used to describe what is presumably a data structure or class for permissions.
- Per rubric item 2 (동작을 대신하는 비유): "입력·저장·호출·반환·검증·노출 같은 동작을 손잡이, 관문, 뼈대, 껍데기 같은 사물이나 이동으로만 설명하는가?"
- "그릇" is exactly the kind of metaphor that replaces actual operation. The reader doesn't know if this is a class, a struct, a database table, a list, a map, etc. What gets stored? Where? How is it accessed?
- Finding: 구체화 필요 - the target (what kind of permissions) and operation (what container, what API) are obscured by the metaphor.

**Sentence 2: "임시 권한은 만료 시각을 저장하고 각 요청에서 현재 시각과 비교해 유효성을 확인합니다."**
- Target: 임시 권한 (temporary permissions)
- Operation: 만료 시각 저장, 각 요청에서 현재 시각과 비교, 유효성 확인
- This sentence actually provides concrete operations: store expiration time, compare with current time per request, verify validity.
- The verb forms are clear (저장하고, 비교해, 확인합니다).
- Reader can understand: temporary permissions store an expiration timestamp, and on each request, the system compares it with the current time to check validity.
- This seems to pass. The information order is OK (subject → operation → condition).
- Finding: 통과

**Sentence 3: "사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 적용해 거부를 우선합니다."**
- Target: 4 cases of permission evaluation
- Operation: 순으로 적용, 거부를 우선
- "거부를 우선합니다" — what does this mean exactly? Priority order? Or within same level, deny wins?
- The ordering shows 1) user-deny, 2) user-allow, 3) role-deny, 4) role-allow
- "거부를 우선합니다" is ambiguous. Does it mean:
  - Earlier position wins? (so user-deny beats user-allow beats role-deny beats role-allow)
  - Any deny beats any allow?
  - When there's a conflict at the same level, deny wins?
- The natural reading seems to be "earlier in the list wins" — but "거부를 우선" literally says "deny takes priority". This is ambiguous about scope.
- Also "사용자 직접 거부, 사용자 직접 허용" — what does "직접" mean here? Direct user assignment vs. role-based? Direct grant? This needs verification but is established terminology in permission systems.
- "역할 거부, 역할 허용" — what does role-level deny mean? Permissions inherited through roles, but role explicitly denies?
- Per rubric item 1 (낯선 결합): "역할 거부" — does role have a "deny"? In typical RBAC, roles grant permissions, not deny. So role-deny is unusual and needs clarification.
- Per rubric item 3 (명사 나열과 과도한 압축): the four cases are listed without explicit subjects.
- Finding: 구체화 필요 or 의미 확인 필요 - the precedence rule is ambiguous, and the meaning of role-deny is unclear.

Let me reconsider sentence 2 more carefully:
- "임시 권한" — what type of permissions are temporary? This is somewhat established in permission systems.
- The operation chain is clear: store expiration time → compare on each request → verify validity
- This is sufficiently clear. Pass.

Sentence 3 — let me think about the precedence rule again.
- 4 items listed in order: 사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용
- "순으로 적용해 거부를 우선합니다"
- The most natural reading: apply in this order, deny has priority
- If "earlier applied first" then user-deny > user-allow > role-deny > role-allow
- If "deny wins over allow" then user-deny > role-deny > user-allow > role-allow
- These are different precedence rules. The original sentence is ambiguous between these.
- Actually, the most natural Korean reading might be: "apply in this order, and priority is given to deny". This could mean within the same level, deny wins. Or it could mean deny (any deny) beats allow (any allow).
- This needs clarification. 의미 확인 필요.

Now, let me also check:
- "사용자 직접 거부" vs "사용자 직접 허용" — "직접" might mean "explicitly" as opposed to inherited. This is somewhat standard in permission systems (like Windows ACL or similar).
- "역할 거부" — this is unusual. Roles typically grant, not deny. Unless it's a deny-role. Needs verification.

Let me draft the response in the default format.

Output format for audit:
```markdown
## 요약
- 구체화 필요 N건, 의미 확인 필요 N건
- 가장 큰 독해 부담: …

| 위치 | 원문 | 독자가 추측해야 하는 정보 | 판정 | 수정안 | 확인할 사실 |
|---|---|---|---|---|---|
```

I should:
1. Only list problematic sentences (skip passing ones, or note them briefly)
2. The user asked to "문제가 없는 문장은 별도로 짧게 표시하세요" — note passing sentences separately and briefly.

Let me write the response.

Let me reconsider the examples once more.

Sentence 1: "권한을 담아낼 그릇이 필요합니다."
- The metaphor "그릇" replaces the actual structure. What type of container? A class? A list? A map? In what context?
- Per rubric 2: 동작을 대신하는 비유 — yes, "그릇" is a metaphor replacing a data structure description.
- Per rubric 3: It's a noun-like statement without explicit operation, though "필요합니다" does provide some verb structure.
- 판정: 구체화 필요
- Suggested revision: Need to know what "permissions" refers to. Could be "권한 항목을 보관할 자료구조가 필요하다" or similar — but I should preserve ambiguity and ask what kind of permissions and what kind of container.

Actually, the revision suggestion should be illustrative, not fabricate. Let me give a generic suggestion: "권한 항목을 보관할 [자료구조/클래스/목록]가 필요하다" or note that the actual type needs to be specified.

Sentence 2: 
"임시 권한은 만료 시각을 저장하고 각 요청에서 현재 시각과 비교해 유효성을 확인합니다."
- Subject: 임시 권한 (what kind? granted tokens? session perms? but contextually clear from "임시")
- Operations: 만료 시각 저장, 비교, 확인
- Clear enough. Pass.

Sentence 3: 
"사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 적용해 거부를 우선합니다."
- Subject/operation: 적용 우선순위
- Four cases listed in order
- "거부를 우선" — ambiguous precedence rule
- "역할 거부" — unusual concept, needs verification

Let me think about the precedence more. The sentence says "순으로 적용해 거부를 우선합니다". In Korean, this could parse as:
1. Apply in order [list], and priority is given to deny.
2. Apply in the order of [list], with priority for deny.
The "순으로 적용" suggests an ordered precedence (first match wins). But "거부를 우선" suggests a different rule (deny beats allow).

If the intended rule is "first match wins in this order", then saying "거부를 우선" is redundant or confusing.
If the intended rule is "any deny beats any allow", then "순으로 적용" is redundant or unnecessary.

The two statements seem to encode different precedence schemes. This is genuinely ambiguous.

One possible intent: Apply these four rules in this order, where within the same source (user vs role), deny wins. But that's reading into it.

I'll mark this as 의미 확인 필요 because the precedence rule itself is genuinely ambiguous from the text.

Let me also consider "사용자 직접 거부" — this likely means "user explicit deny" (as in Windows ACL or similar). "사용자 직접 허용" = "user explicit allow". This terminology is established in permission systems. So I won't flag the terminology itself, but the precedence ambiguity and the role-deny concept.

Actually, "역할 거부" is interesting. In RBAC, roles typically grant permissions. So "역할 거부" might mean:
- A deny role assignment
- An inherited deny through role membership
- A role-level deny rule

This is genuinely ambiguous and needs context.

Let me finalize my response.

Actually, looking again at sentence 1: "권한을 담아낼 그릇이 필요합니다."
- This is a very short sentence with a single metaphor.
- The target is unclear: what permissions? System permissions? UI permissions? API permissions?
- The operation is unclear: what container? A class? A list? A database table?
- 판정: 구체화 필요 (we know what's meant generally, but the specific implementation is hidden)

For the suggested revision, I'll note it should specify the structure.

Let me also reconsider sentence 2 — is "임시 권한" too abstract? "임시 권한" is a reasonable term for "temporary/ephemeral permissions". The rest is concrete. I'll mark it as 통과.

OK, let me write the final response in the required format.

Format reminder:
- Summary section with counts
- Table with columns: 위치 | 원문 | 독자가 추측해야 하는 정보 | 판정 | 수정안 | 확인할 사실
- Only list problematic sentences; passing ones can be noted separately briefly

The user also asked: "문제가 없는 문장은 별도로 짧게 표시하세요." So I should note passing sentences briefly.</think>

## 요약
- 구체화 필요 1건, 의미 확인 필요 1건
- 가장 큰 독해 부담: 1번의 비유가 대상과 자료구조를 통째로 가리고, 3번의 우선순위 규칙이 "순서 우선"인지 "거부 우선"인지 단정되지 않음

## 통과 문장
- **2번**: 주체(임시 권한)와 동작(만료 시각 저장 → 요청별 현재 시각 비교 → 유효성 확인)이 한 문장 안에서 분명하게 드러나며, 독자가 별도 맥락 없이도 처리 흐름을 복원할 수 있음.

## 문제 문장

| 위치 | 원문 | 독자가 추측해야 하는 정보 | 판정 | 수정안 | 확인할 사실 |
|---|---|---|---|---|---|
| 1 | 권한을 담아낼 그릇이 필요합니다. | ① 어떤 단위의 권한인지(액션 단위, 리소스 단위, 토큰 단위 등) ② "그릇"이 가리키는 구현체가 무엇인지(클래스, 맵, 목록, DB 테이블 등) ③ 누가 어디에 보관하며 어떤 API로 채우고 비우는지가 모두 사라짐 | 구체화 필요 | "권한 항목(예: `{action, resource}` 쌍)을 보관할 자료구조가 필요하다. `Permission` 같은 단일 객체로 표현할지, `Map<Resource, Set<Action>>`처럼 묶을지는 구현 단계에서 정한다." 와 같이 대상 단위와 보관 방식을 명시 | 이 "권한"이 어떤 시스템의 어느 추상화 층에 존재하는지(도메인 모델, 인증 토큰, ACL 등) |
| 3 | 사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 적용해 거부를 우선합니다. | ① "순으로 적용"과 "거부를 우선"이 같은 규칙인지 별개 규칙인지 모호 — 같은 출처 내 deny 우선인지, 모든 deny가 모든 allow를 이기는지 ② "역할 거부"가 무엇인지(RBAC에서 역할은 보통 부여만 하는데, 여기서 deny를 뜻하는지 별도의 Deny-role인지) ③ "적용"이 첫 매치 적용인지, 누적 적용인지 | 의미 확인 필요 | 우선 적용이 단일 규칙이라면: "같은 사용자·같은 요청에 대해 (1) 사용자 직접 deny → (2) 사용자 직접 allow → (3) 역할 deny → (4) 역할 allow 순으로 첫 번째 매치를 사용한다." 또는 별개 규칙이라면 두 문장으로 분리: "위 순서대로 평가하되, 같은 출처 안에서는 deny를 allow보다 우선한다." | ① 우선 적용 알고리즘이 first-match인지 deny-overrides-allow인지 ② RBAC 시스템에서 "역할 deny"가 실제로 지원되는 개념인지, 지원된다면 그 표현 방식이 무엇인지 |
