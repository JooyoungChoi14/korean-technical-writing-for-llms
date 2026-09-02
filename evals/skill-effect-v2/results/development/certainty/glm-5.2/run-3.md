```json
{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "‘다리’가 실제로 어떤 구성 요소나 메커니즘인지(예: API 엔드포인트, 메시지 큐, 파이프라인 단계)",
      "suggested_revision": null,
      "verification_question": "정산 결과를 다음 단계로 전달하는 구체적인 수단(예: API, 메시지 큐, 파이프라인 단계)은 무엇입니까?"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "‘완충지대’가 실제로 어떤 구성 요소인지(예: 예외 처리기, 데드 레터 큐, 폴백 로직)",
      "suggested_revision": null,
      "verification_question": "예외를 수신·처리하는 구체적인 구성 요소(예: 예외 처리기, 데드 레터 큐, 폴백 큐)는 무엇입니까?"
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "‘손잡이’가 실제로 어떤 API나 속성인지, ‘끌어올린다’가 어떤 동작(예: 조회, 응답, 상태 공개)인지",
      "suggested_revision": null,
      "verification_question": "통계 값을 화면에 제공하는 구체적인 수단(예: API 엔드포인트, 상태 속성, 데이터 조회 쿼리)은 무엇입니까?"
    },
    {
      "id": "DEV-P01",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "DEV-P02",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "DEV-P03",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "DEV-C01",
      "decision": "구체화 필요",
      "reader_must_infer": "‘순으로 적용’이 각 단계가 순차적으로 결과를 변경하는 방식인지, 나열된 순서대로 첫 번째 일치 규칙만 적용하는 방식인지. ‘제외 조건을 할인보다 우선’이 나열 순서와 어떻게 다른지",
      "suggested_revision": null,
      "verification_question": "‘순으로 적용’은 각 규칙이 순차적으로 가격을 변경하는 방식입니까, 아니면 나열된 순서대로 첫 번째 일치 규칙만 적용하는 방식입니까? ‘제외 조건을 할인보다 우선’은 나열 순서와 어떻게 다르게 동작합니까?"
    },
    {
      "id": "DEV-C02",
      "decision": "구체화 필요",
      "reader_must_infer": "‘순으로 판정’이 나열된 순서대로 첫 번째 일치 규칙을 선택하는 것인지, 모든 규칙을 순차적으로 평가하는 것인지. ‘보류를 승인보다 우선’이 나열 순서(수동 승인이 1순위, 자동 보류가 2순위)와 어떻게 다른지",
      "suggested_revision": null,
      "verification_question": "‘순으로 판정’은 나열된 순서대로 첫 번째 일치 규칙만 선택하는 방식입니까, 아니면 모든 규칙을 순차적으로 평가한 뒤 최종 결과를 정하는 방식입니까? ‘보류를 승인보다 우선’은 나열 순서와 어떻게 다르게 동작합니까?"
    },
    {
      "id": "DEV-C03",
      "decision": "구체화 필요",
      "reader_must_infer": "‘순으로 적용’이 순차 적용인지 우선순위 기반 선택인지. ‘차단을 항상 우선’이 나열 순서(조직 차단이 2순위, 기본 차단이 4순위)와 어떻게 다른지. ‘항상’의 정확한 조건",
      "suggested_revision": null,
      "verification_question": "‘순으로 적용’은 각 규칙이 순차적으로 적용 결과를 변경하는 방식입니까, 아니면 나열된 순서대로 첫 번째 일치 규칙만 적용하는 방식입니까? ‘차단을 항상 우선’은 허용 규칙이 먼저 일치해도 차단 규칙이 있으면 차단한다는 뜻입니까?"
    },
    {
      "id": "DEV-N01",
      "decision": "구체화 필요",
      "reader_must_infer": "주체와 서술어가 생략되어, 시스템이 수정을 차단하는지 정책상 금지인지, 취소 후 재작성의 주체가 누구인지",
      "suggested_revision": "월말 마감 이후에는 전표를 수정할 수 없으며, 오류가 있는 전표는 취소한 뒤 다시 작성합니다.",
      "verification_question": null
    },
    {
      "id": "DEV-P04",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "DEV-P05",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    }
  ]
}
```
