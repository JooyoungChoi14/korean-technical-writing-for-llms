{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "'다리'가 의미하는 기술적 구성 요소 (API, 큐, 파일 등)",
      "suggested_revision": "정산 결과를 다음 단계로 전달할 인터페이스가 필요합니다.",
      "verification_question": "'다리'가 구체적으로 어떤 전송 매커니즘을 의미합니까?"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "'완충지대'가 의미하는 예외 처리 구조",
      "suggested_revision": "예외 발생 시 처리할 오류 핸들러를 둡니다.",
      "verification_question": "'완충지대'가 try-catch 블록인지 별도 큐인지 명확합니까?"
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "'손잡이'가 의미하는 조회 수단",
      "suggested_revision": "통계 값을 화면에서 조회할 수 있는 API 엔드포인트를 추가합니다.",
      "verification_question": "'손잡이'가 API 인지 UI 버튼인지 명확합니까?"
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
      "reader_must_infer": "할인 적용 순서와 기본 가격의 역할",
      "suggested_revision": "기본 가격을 기준으로 개별 상품 할인과 회원 등급 할인을 적용하며, 캠페인 제외 조건은 할인 적용 전에 우선 평가합니다.",
      "verification_question": "'기본 가격 순으로 적용'의 실제 계산 로직 순서는 무엇입니까?"
    },
    {
      "id": "DEV-C02",
      "decision": "구체화 필요",
      "reader_must_infer": "규칙 평가 순서와 기본 거절의 시점",
      "suggested_revision": "승인 여부를 수동 승인, 자동 보류, 부서 승인 순으로 평가하며, 조건에 만족하지 않으면 기본 거절합니다. 보류 조건은 승인 조건보다 우선합니다.",
      "verification_question": "'순으로 판정'이 규칙 평가 순서인지 결과 우선순위인지?"
    },
    {
      "id": "DEV-C03",
      "decision": "구체화 필요",
      "reader_must_infer": "정책 평가 순서와 기본값의 역할",
      "suggested_revision": "알림 허용 여부를 사용자, 조직, 채널 순으로 평가하며, 조건에 만족하지 않으면 기본 차단합니다. 차단 조건은 허용 조건보다 우선합니다.",
      "verification_question": "'순으로 적용'이 평가 순서인지 우선순위인지?"
    },
    {
      "id": "DEV-N01",
      "decision": "구체화 필요",
      "reader_must_infer": "주체 (시스템 제약인지 운영 지침인지)",
      "suggested_revision": "월말 마감 이후에는 전표를 수정할 수 없으며, 오류가 있는 전표는 취소한 후 다시 작성해야 합니다.",
      "verification_question": "이 규칙이 시스템 제약인지 운영 방침인지?"
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
