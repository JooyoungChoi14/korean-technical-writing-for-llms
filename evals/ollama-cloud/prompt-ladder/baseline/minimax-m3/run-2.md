<think>릇" = container) that doesn't specify what the actual target is
- Finding: 동작을 대신하는 비유 (metaphor replacing operation)
- Verdict: 구체화 필요

**Sentence 2: "임시 권한은 만료 시각을 저장하고 각 요청에서 현재 시각과 비교해 유효성을 확인합니다."**
- Target: 임시 권한 (temporary permission)
- Operation: 만료 시각 저장, 현재 시각과 비교, 유효성 확인
- Actors: 시스템 (implied)
- This is fairly clear. The subject is "임시 권한" which is a bit abstract - does it mean the system managing temporary permissions? But the meaning is clear: temporary permissions store an expiration time and compare it with the current time on each request.
- Actually, this is acceptable. The subject "임시 권한" is slightly abstract but the operations are clearly stated (저장, 비교, 확인).
- I think this passes or is close to passing. The subject performing these actions is implied to be the permission system. Let me think again...
- "임시 권한은 만료 시각을 저장하고" - 임시 권한 is the subject doing the storing. This is a bit odd because typically a system stores data, not the data itself. But in Korean technical writing, this kind of subject is acceptable as shorthand for "임시 권한 데이터는" or "임시 권한 시스템은".
- The operations are clear: 저장, 비교, 확인
- I think this is acceptable - 통과 or borderline.

Actually, let me reconsider. "임시 권한은 만료 시각을 저장하고" - this could be slightly awkward because temporary permissions don't actively store things; a system does. But this is a common Korean technical writing style and the meaning is clear.

I'll say this passes.

**Sentence 3: "사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 적용해 거부를 우선합니다."**
- Target: 권한 결정 규칙
- Operation: 순서대로 적용, 거부 우선
- "거부를 우선합니다" - what does "우선" mean here? Does it mean earlier in the list takes precedence? Or does "거부" always win regardless of order?
- Reader must infer: the precedence rule. Looking at the list: user-deny, user-allow, role-deny, role-allow. "거부를 우선합니다" likely means user-deny takes precedence over user-allow, and role-deny takes precedence over role-allow.
- Actually, looking more carefully: the order suggests 1) user-deny, 2) user-allow, 3) role-deny, 4) role-allow, with deny taking priority at each level.
- But "거부를 우선합니다" is ambiguous - is it denying wins at each pair, or the order itself is the priority?
- The phrase "순으로 적용해 거부를 우선합니다" combines two concepts: order and priority. The "순으로 적용" means applying in order, and "거부를 우선" means deny takes priority. But how do these interact?
- I think the meaning is: apply in this order (1→4), and at each level deny wins. Or: first check user-deny, then user-allow, then role-deny, then role-allow, but deny trumps allow.
- This needs clarification - the precedence rule is ambiguous.
- Verdict: 구체화 필요

Let me also consider:
- "사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 적용해 거부를 우선합니다."
- This describes a permission evaluation algorithm.
- The order: user-direct-deny, user-direct-allow, role-deny, role-allow
- "거부를 우선" - deny wins
- But the relationship between the order and the priority is unclear
- Possible interpretations:
  a) Check in this order, but at each pair (user, role), deny wins over allow
  b) Apply in this strict order; the first matching rule wins
  c) Evaluate all four, then deny takes priority regardless of order

This is genuinely ambiguous. The reader needs to understand the precedence rule.

Now let me write the response.

For Sentence 1:
- 위치: 1번 문장
- 원문: 권한을 담아낼 그릇이 필요합니다.
- 독자가 추측해야 하는 정보: 무엇을 위한 어떤 종류의 자료구조/시스템 구성요소인가
- 판정: 구체화 필요
- 수정안: 예) "권한 정보를 보관할 데이터 구조가 필요합니다" 또는 더 구체적으로
- 확인할 사실: 권한을 어떤 단위로 저장할 것인가(테이블, 토큰, 객체 등)

For Sentence 2:
- 통과. 동작과 조건이 명확함.

For Sentence 3:
- 위치: 3번 문장
- 원문: 사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 적용해 거부를 우선합니다.
- 독자가 추측해야 하는 정보: "순으로 적용"과 "거부를 우선"의 정확한 결합 방식 (각</think>

<think> 쌍에서 거부가 이기는지, 순서대로 매칭되는 첫 번째 규칙이 이기는지)
- 판정: 의미 확인 필요 (or 구체화 필요)
- 수정안: "사용자별 거부 설정을 먼저 확인하고, 없으면 사용자별 허용 설정을 확인하고, 없으면 역할 기반 거부 설정을 확인하고, 없으면 역할 기반 허용 설정을 적용한다." 또는 "거부 설정이 허용 설정보다 항상 우선한다."
- 확인할 사실: 우선순위 규칙의 정확한 작동 방식

Let me draft the response:

```markdown
## 요약
- 구체화 필요 1건, 의미 확인 필요 1건
- 가장 큰 독해 부담: 비유("그릇")로 대상이 가려진 점과, 우선순위 규칙의 작동 방식이 모호한 점

| 위치 | 원문 | 독자가 추측해야 하는 정보 | 판정 | 수정안 | 확인할 사실 |
|---|---|---|---|---|---|
| 1 | 권한을 담아낼 그릇이 필요합니다. | 어떤 종류의 보관 구조(테이블, 토큰, 객체 등)인지, 어떤 단위/속성으로 구성되는지 | 구체화 필요 | 권한 정보를 보관할 데이터 구조가 필요합니다. | 보관 대상의 단위(역할 단위, 사용자 단위, 토큰 등)와 저장 위치 |
| 3 | 사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 적용해 거부를 우선합니다. | "순으로 적용"과 "거부를 우선"의 결합 방식 (각 쌍에서 거부가 이기는지, 순서대로 매칭되는 첫 항목이 이기는지) | 의미 확인 필요 | 예: "권한 평가는 ① 사용자 직접 거부 → ② 사용자 직접 허용 → ③ 역할 거부 → ④ 역할 허용 순으로 확인하고, 같은 사용자에 대해 거부 설정이 허용 설정보다 항상 우선한다." | 우선순위 결합 방식, 동일 사용자에 거부/허용이 동시에 설정될 때의 동작 |

## 통과한 문장
- 2번: "임시 권한은 만료 시각을 저장하고 각 요청에서 현재 시각과 비교해 유효성을 확인합니다." — 동작(저장·비교·확인), 조건(각 요청), 결과(유효성 확인)가 모두 드러나 있음.
```

Let me check if my analysis is correct:

For Sentence 1, "그릇" is a metaphor replacing what kind of data structure is needed. The reader cannot know if this is a database table, a token, a variable, a class, etc. This is a "동작을 대신하는 비유" pattern from rubric.

For Sentence 3, the priority rule is genuinely ambiguous. "순으로 적용해 거부를 우선합니다" - this could mean:
- Check in this order; first match wins (so user-deny beats user-allow because it's listed first)
- Or: check in this order; at each level (user/role), deny beats allow

These are different algorithms. This requires confirmation.

Let me finalize. I should make sure my response is in Korean as the user requested in Korean.

Actually wait, let me re-examine sentence 3 more carefully:
"사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 적용해 거부를 우선합니다."

Reading this as a standard permission precedence rule:
- Order: user-deny, user-allow, role-deny, role-allow
- "거부를 우선" = deny takes priority

The most common interpretation in authorization systems (like RBAC with allow/deny overrides):
- First check user-deny (highest priority)
- Then user-allow
- Then role-deny
- Then role-allow (lowest priority)

So the order itself might already encode the priority, and "거부를 우선" emphasizes that deny wins over allow at each level.

But this is still ambiguous to the reader because the relationship between "순으로 적용" and "거부를 우선" isn't explicit. Are they the same rule (order = priority) or two separate rules (apply in order, AND deny wins)?

I'll mark this as 의미 확인 필요 because the natural reading is uncertain.

Let me also reconsider sentence 2:

"임시 권한은 만료 시각을 저장하고 각 요청에서 현재 시각과 비교해 유효성을 확인합니다."

The subject "임시 권한" performing actions "저장하고" "비교해" "확인합니다" - in Korean, this kind of construct where a noun phrase is the subject of an action verb is acceptable in technical writing. The reader understands this as "the temporary permission system/module" or "temporary permission records."

Actually, I realize "임시 권한은" could be interpreted as:
- 임시 권한 (the data/record) stores... (unusual but possible)
- 임시 권한 (the system feature) stores... 

The action "만료 시각을 저장하고" - storing something implies a system or storage mechanism. This slight subject-action mismatch exists but is not severe enough to flag.

Operations are clear:
- 만료 시각 저장 (stores expiration time)
- 현재 시각과 비교 (compares with current time)
- 유효성 확인 (verifies validity)

Conditions: 각 요청에서 (on each request)
Result: 유효성 확인 (validity check)

This sentence is clear. 통과.

OK, my analysis is solid. Let me write the final response.

One more thing to consider: for Sentence 3, looking at common Korean authorization docs, "순으로 적용해 거부를 우선" most likely means "apply in this order, with deny taking precedence." So the natural reading is:
1. Check user-deny
2. If no user-deny, check user-allow
3. If no user-allow, check role-deny
4. If no role-deny, check role-allow

But "거부를 우선" reinforces that within the same scope (user or role), deny beats allow. This is somewhat redundant with the order but emphasizes the rule.

Still, the relationship between order and priority is ambiguous. A reader might wonder: is this order strict first-match, or is it priority-based with deny winning?

I'll keep this as 의미 확인 필요.

Actually, I'll reclassify it. Let me look at the rubric:
- 구체화 필요: 뜻은 확정할 수 있으나 대상·동작·조건·결과 일부가 표현에 가려졌다
- 의미 확인 필요: 자연스럽게 고칠 수는 있지만 원문만으로 정확한 뜻을 확정할 수 없다

For Sentence 3, the meaning CAN be fixed naturally (it's a precedence rule), but the exact mechanism is not determinable from the text alone. So 의미 확인 필요 is appropriate.

Hmm, but I think there's also an argument for 구체화 필요 - the meaning can be inferred (priority with deny winning) but the exact precedence logic is obscured.

Let me go with 의미 확인 필요 because the natural rewriting requires knowing the exact precedence rule, which the source doesn't specify.

OK let me write the final response now.

Wait, I should also think about whether "순으로 적용해" + "거부를 우선" creates a logical conflict. If applied strictly in order, then user-deny is checked first and if it matches, nothing else matters. Then user-allow, etc. In this case, "거부를 우선" is somewhat redundant because the order already puts deny first. Unless "거부를 우선" means "at each level (user/role), deny wins over allow" - which is a separate rule.

I think this is genuinely ambiguous and requires confirmation.

Final response coming up.```</think>

markdown
## 요약
- 구체화 필요 1건, 의미 확인 필요 1건
- 가장 큰 독해 부담: "그릇"이라는 비유로 보관 대상의 정체성이 가려진 점, 그리고 "순으로 적용"과 "거부를 우선"이 결합되는 정확한 방식이 드러나지 않는 점

| 위치 | 원문 | 독자가 추측해야 하는 정보 | 판정 | 수정안 | 확인할 사실 |
|---|---|---|---|---|---|
| 1 | 권한을 담아낼 그릇이 필요합니다. | 보관 대상의 단위(역할/사용자/토큰 등)와 보관 형태(테이블, 캐시, 객체 등) | 구체화 필요 | 권한 정보를 보관할 저장소가 필요합니다. (또는 "권한 항목을 보관할 데이터 구조를 정의해야 합니다.") | 어떤 단위로 권한을 보관할 것인지, 어디에 저장할 것인지 |
| 3 | 사용자 직접 거부, 사용자 직접 허용, 역할 거부, 역할 허용 순으로 적용해 거부를 우선합니다. | "순으로 적용"이 첫 번째 매칭 우선(엄격 순서)인지, "거부를 우선"이 같은 범위(사용자/역할) 내에서 거부>허용을 의미하는 별도 규칙인지 | 의미 확인 필요 | 예: "권한 평가는 ① 사용자 직접 거부 → ② 사용자 직접 허용 → ③ 역할 거부 → ④ 역할 허용 순으로 확인하며, 같은 범위에서는 거부 설정이 허용 설정보다 항상 우선한다." | 우선순위 결합 방식(엄격 순서 vs. 범위별 거부 우선), 동일 항목에 거부/허용이 동시 설정된 경우의 동작 |

## 통과한 문장
- **2번**: "임시 권한은 만료 시각을 저장하고 각 요청에서 현재 시각과 비교해 유효성을 확인합니다." — 동작(저장·비교·확인), 트리거 조건(각 요청), 결과(유효성 확인)가 모두 드러나 있음.
```
