{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "'다리'가 의미하는 구체적인 기술 수단 (API, 파일 적재, 이벤트 등) 과 전달 방향",
      "suggested_revision": "정산 결과를 다음 단계로 전달할 인터페이스 (또는 API) 가 필요합니다.",
      "verification_question": null
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "'완충지대'가 의미하는 오류 처리 메커니즘 (try-catch, 대기 큐, 로깅 등)",
      "suggested_revision": "예외 발생 시 처리할 오류 핸들러 (또는 대기 큐) 를 둡니다.",
      "verification_question": null
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "'손잡이'가 의미하는 데이터 조회 수단 (API 엔드포인트, 함수, UI 컨트롤 등)",
      "suggested_revision": "통계 값을 화면에 표시할 조회 API (또는 함수) 를 추가합니다.",
      "verification_question": null
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
      "decision": "의미 확인 필요",
      "reader_must_infer": "'기본 가격'이 계산의 기준인지 아니면 적용 순서의 마지막 단계인지",
      "suggested_revision": "기본 가격을 기준으로 개별 상품 할인과 회원 등급 할인을 적용하며, 캠페인 제외 조건이 할인보다 우선합니다.",
      "verification_question": "'기본 가격 순으로 적용'이란 기본 가격을 기준으로 할인을 적용한다는 뜻입니까, 아니면 계산 단계의 마지막에 기본 가격이 결정된다는 뜻입니까?"
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
      "reader_must_infer": "주체 (시스템 또는 사용자) 와 명확한 서술어",
      "suggested_revision": "월말 마감 이후에는 전표를 수정할 수 없으며, 오류가 있는 전표는 취소한 후 다시 작성해야 합니다.",
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
