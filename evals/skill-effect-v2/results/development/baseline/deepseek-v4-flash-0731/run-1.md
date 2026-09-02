{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "‘다리’가 구체적으로 무엇을 의미하는지(어떤 모듈, 인터페이스, 데이터 전달 방식) 추측해야 한다.",
      "suggested_revision": "정산 결과를 다음 단계로 전달하는 인터페이스를 추가합니다.",
      "verification_question": "‘다리’가 실제로 추가해야 하는 것은 API, 메시지 큐, 함수 호출 중 무엇입니까?"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "‘완충지대’가 예외를 처리하는 구체적인 동작(로깅, 재시도, 변환)을 대신하고 있어 독자가 실제 처리 방식을 추측해야 한다.",
      "suggested_revision": "예외를 받아서 기록하고 재시도할 수 있는 처리 구간을 둡니다.",
      "verification_question": "‘완충지대’에서 예외를 어떻게 처리해야 합니까? (기록, 재시도, 변환 등)"
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "‘손잡이’가 통계 값을 화면에 전달하는 구체적인 메커니즘(API, 상태 공개, 이벤트)을 추측해야 한다.",
      "suggested_revision": "통계 값을 화면에서 읽을 수 있도록 조회 API를 추가합니다.",
      "verification_question": "‘손잡이’가 의미하는 것은 API 엔드포인트, 상태 변수 공개, 이벤트 발행 중 무엇입니까?"
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
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
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
      "reader_must_infer": "‘불가’와 ‘재작성’의 주체와 조건(누가, 언제, 어떤 시스템에서)이 생략되어 독자가 채워야 한다.",
      "suggested_revision": "월말 마감 이후에는 전표를 수정할 수 없으며, 오류 전표는 취소한 뒤 재작성해야 합니다.",
      "verification_question": "이 규칙의 적용 대상은 모든 사용자입니까, 특정 권한을 가진 사용자만입니까?"
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
