{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "'다리'가 의미하는 기술적 메커니즘 (API, 파일 전송, 이벤트 등)",
      "suggested_revision": "정산 결과를 다음 단계로 전달할 인터페이스가 필요합니다.",
      "verification_question": "전달 메커니즘의 구체적인 기술 수단 (API, 배치, 메시지 큐 등) 은 무엇입니까?"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "'완충지대'가 의미하는 예외 처리 구성 요소",
      "suggested_revision": "예외 발생 시 처리할 오류 핸들러를 둡니다.",
      "verification_question": "예외를 격리하거나 처리하는 구체적인 컴포넌트 (큐, 로거, 서비스 등) 는 무엇입니까?"
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "'손잡이'가 의미하는 데이터 조회 수단",
      "suggested_revision": "통계 값을 화면에 조회할 API 엔드포인트를 추가합니다.",
      "verification_question": "화면 연동을 위한 기술적 수단 (API, 함수, 뷰 등) 은 무엇입니까?"
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
      "reader_must_infer": "'기본 가격 순으로'의 의미 (계산 기준인지 적용 단계인지)",
      "suggested_revision": "기본 가격을 기준으로 캠페인 제외 조건, 개별 상품 할인, 회원 등급 할인 순으로 적용하며 제외 조건을 할인보다 우선합니다.",
      "verification_question": "기본 가격 계산은 할인 적용 전 단계이며, 적용 순서에서 제외됩니까?"
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
      "decision": "구체화 필요",
      "reader_must_infer": "문장의 주체 (시스템 제한인지 정책인지) 와 동작 (수정 불가, 재작성 필요)",
      "suggested_revision": "월말 마감 이후에는 전표를 수정할 수 없습니다. 오류 전표는 취소한 후 재작성해야 합니다.",
      "verification_question": "수정 불가 주체는 시스템이며, 재작성 행위 주체는 사용자입니까?"
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
