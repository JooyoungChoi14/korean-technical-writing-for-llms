{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "정산 결과를 전달할 실제 기술 수단 (API, DB 테이블, 이벤트 큐 등)",
      "suggested_revision": "정산 결과를 다음 단계로 전달할 인터페이스 (또는 테이블/큐) 를 마련합니다.",
      "verification_question": "정산 결과를 다음 단계로 넘기는 실제 기술 수단은 무엇입니까?"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "예외를 처리할 구체적인 메커니즘 (try-catch, 오류 큐, 재시도 로직 등)",
      "suggested_revision": "예외 발생 시 작업을 중단하지 않고 오류 큐에 저장하거나 재시도 로직으로 처리합니다.",
      "verification_question": "예외를 받아내는 구체적인 처리 메커니즘은 무엇입니까?"
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "통계 값을 화면에 노출하는 실제 인터페이스 (API 파라미터, UI 컴포넌트, getter 등)",
      "suggested_revision": "통계 값을 화면에서 읽을 수 있도록 조회 API 또는 속성을 추가합니다.",
      "verification_question": "통계 값을 화면으로 가져오는 실제 인터페이스는 무엇입니까?"
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
      "reader_must_infer": "할인 적용 순서와 기본 가격의 계산 기준 관계",
      "suggested_revision": "기본 가격을 기준으로 개별 상품 할인, 회원 등급 할인을 적용하며 캠페인 제외 조건을 할인보다 우선합니다.",
      "verification_question": "기본 가격은 계산의 시작점입니까, 아니면 적용 단계 중 하나입니까?"
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
      "reader_must_infer": "수정 불가의 주체 (사용자/시스템) 와 오류 전표 처리 주체",
      "suggested_revision": "월말 마감 이후에는 전표를 수정할 수 없습니다. 오류 전표는 취소한 후 다시 작성합니다.",
      "verification_question": "오류 전표의 취소 처리는 누가 수행합니까?"
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
