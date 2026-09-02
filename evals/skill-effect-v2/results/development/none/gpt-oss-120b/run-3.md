{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "‘다리’가 구체적으로 어떤 컴포넌트 또는 인터페이스를 의미하는지",
      "suggested_revision": "정산 결과를 다음 단계로 전달하기 위한 인터페이스가 필요합니다.",
      "verification_question": "‘다리’가 구체적으로 어떤 모듈 또는 기능을 의미합니까?"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "‘완충지대’가 적용되는 레이어나 위치가 명시되지 않음",
      "suggested_revision": "예외를 처리하기 위해 오류 처리 레이어를 추가합니다.",
      "verification_question": "‘완충지대’가 적용되는 구체적인 위치와 동작은 무엇입니까?"
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "‘손잡이’가 의미하는 UI 요소가 불분명함",
      "suggested_revision": "통계 값을 화면에 표시하기 위한 UI 핸들을 추가합니다.",
      "verification_question": "‘손잡이’가 구체적으로 어떤 UI 요소를 가리킵니까?"
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
      "reader_must_infer": "‘제외 조건’이 구체적으로 어떤 상황을 의미하는지",
      "suggested_revision": "가격 계산 시 개별 상품 할인 → 회원 등급 할인 → 캠페인 제외 → 기본 가격 순으로 적용하되, 할인 적용보다 제외 조건을 우선 적용합니다.",
      "verification_question": "‘제외 조건’이 구체적으로 어떤 상황을 의미합니까?"
    },
    {
      "id": "DEV-C02",
      "decision": "구체화 필요",
      "reader_must_infer": "‘보류’를 승인보다 우선한다는 구체적인 처리 흐름이 명시되지 않음",
      "suggested_revision": "판정 로직은 수동 승인 → 자동 보류 → 부서 승인 → 기본 거절 순으로 진행하며, 보류 상태가 승인보다 우선적으로 처리됩니다.",
      "verification_question": "‘보류’를 승인보다 우선한다는 구체적인 처리 흐름은 어떻게 됩니까?"
    },
    {
      "id": "DEV-C03",
      "decision": "구체화 필요",
      "reader_must_infer": "‘차단’이 적용되는 구체적인 조건이 불명확함",
      "suggested_revision": "알림 설정은 사용자 알림 허용 → 조직 알림 차단 → 채널 허용 → 기본 차단 순으로 적용하며, 차단 규칙은 항상 우선합니다.",
      "verification_question": "‘차단’이 적용되는 구체적인 조건은 무엇입니까?"
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
