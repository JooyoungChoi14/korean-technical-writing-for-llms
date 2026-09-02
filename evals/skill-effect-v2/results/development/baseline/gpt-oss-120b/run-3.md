```json
{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "‘다리’가 구체적으로 어떤 인터페이스·구성 요소를 의미하는지",
      "suggested_revision": "정산 결과를 다음 단계로 전달하기 위한 인터페이스가 필요합니다.",
      "verification_question": "다음 단계는 어떤 시스템이며, 전달 방식은 무엇인가요?"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "‘완충지대’가 어떤 예외 처리 메커니즘을 가리키는지",
      "suggested_revision": "예외를 처리하기 위한 예외 처리 레이어를 추가합니다.",
      "verification_question": "예외 처리 레이어는 어떤 범위·형태의 예외를 잡으며, 어떻게 동작합니까?"
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "‘손잡이’가 구체적으로 어떤 API·엔드포인트를 의미하는지",
      "suggested_revision": "통계 값을 화면에 표시하기 위한 API 엔드포인트를 추가합니다.",
      "verification_question": "통계 값은 어떤 형식으로 제공되며, 어느 화면에 표시됩니까?"
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
      "reader_must_infer": "‘제외 조건’이 구체적으로 무엇을 의미하는지",
      "suggested_revision": "할인 적용 순서는 개별 상품 할인 → 회원 등급 할인 → 캠페인 제외 → 기본 가격이며, 할인 적용 전에 캠페인 제외 조건을 먼저 평가합니다.",
      "verification_question": "‘제외 조건’에 해당하는 구체적인 규칙은 무엇인가요?"
    },
    {
      "id": "DEV-C02",
      "decision": "구체화 필요",
      "reader_must_infer": "‘보류’를 승인보다 우선한다는 구체적인 처리 로직",
      "suggested_revision": "결정 순서는 수동 승인 → 자동 보류 → 부서 승인 → 기본 거절이며, 보류 상태가 발생하면 승인보다 우선적으로 처리됩니다.",
      "verification_question": "‘자동 보류’와 ‘수동 승인’이 동시에 발생할 경우 구체적인 처리 흐름은 어떻게 됩니까?"
    },
    {
      "id": "DEV-C03",
      "decision": "구체화 필요",
      "reader_must_infer": "‘차단’이 적용되는 구체적인 조건",
      "suggested_revision": "알림 적용 순서는 사용자 알림 허용 → 조직 알림 차단 → 채널 허용 → 기본 차단이며, 차단 설정이 있으면 항상 최우선으로 적용됩니다.",
      "verification_question": "‘차단’이 적용되는 구체적인 상황이나 조건은 무엇입니까?"
    },
    {
      "id": "DEV-N01",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
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
