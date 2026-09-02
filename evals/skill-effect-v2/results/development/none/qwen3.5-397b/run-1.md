{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "독자가 '다리'가 구체적으로 어떤 기술적 수단 (API, 큐, 미들웨어 등) 을 의미하는지 추측해야 함.",
      "suggested_revision": "정산 결과를 다음 단계로 전달할 인터페이스 (또는 메시지 큐) 가 필요합니다.",
      "verification_question": "'다리'가 의미하는 구체적인 기술 구성 요소는 무엇입니까?"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "독자가 '완충지대'가 예외 처리 로직, 큐, 또는 임시 저장소를 의미하는지 추측해야 함.",
      "suggested_revision": "예외 발생 시 처리할 수 있는 오류 처리 로직 (또는 데드 레터 큐) 을 구현합니다.",
      "verification_question": "'완충지대'가 의미하는 구체적인 예외 처리 메커니즘은 무엇입니까?"
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "독자가 '손잡이'가 UI 기능인지 API 인지 추측해야 함.",
      "suggested_revision": "통계 값을 화면에 표시하거나 추출할 수 있는 기능 (또는 버튼) 을 추가합니다.",
      "verification_question": "'손잡이'가 의미하는 구체적인 사용자 인터페이스 요소 또는 기능은 무엇입니까?"
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
      "reader_must_infer": "독자가 할인 적용 순서와 제외 조건 확인 시점을 정확히 이해해야 함.",
      "suggested_revision": "기본 가격을 기준으로 캠페인 제외 조건을 먼저 확인한 후, 개별 상품 할인 및 회원 등급 할인을 순차적으로 적용합니다.",
      "verification_question": "할인 적용 순서와 제외 조건 검증 시점이 명확합니까?"
    },
    {
      "id": "DEV-C02",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "DEV-C03",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
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
