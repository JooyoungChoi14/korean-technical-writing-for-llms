{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "'다리'가 의미하는 실제 기술 수단 (API, DB 테이블, 이벤트 큐 등)",
      "suggested_revision": "정산 결과를 다음 단계로 전달할 인터페이스가 필요합니다.",
      "verification_question": "'다리'가 구체적으로 어떤 기술 수단 (API, DB, 메시지 큐 등) 을 의미합니까?"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "'완충지대'가 의미하는 예외 처리 구체적 방식 (로그 저장, 재시도, 무시 등)",
      "suggested_revision": "예외를 처리할 오류 핸들러를 둡니다.",
      "verification_question": "예외 발생 시 구체적으로 어떤 동작 (로그 기록, 재시도, 알림 등) 을 수행합니까?"
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "'손잡이'가 의미하는 기술 구성 요소 (API 엔드포인트, UI 버튼, 함수 등)",
      "suggested_revision": "통계 값을 화면에 표시할 조회 기능을 추가합니다.",
      "verification_question": "'손잡이'가 백엔드 API 인지 프론트엔드 UI 요소인지 명확합니까?"
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
      "reader_must_infer": "목록 순서 (할인→제외) 와 우선순위 문장 (제외→할인) 의 관계, '기본 가격 순으로 적용'의 의미",
      "suggested_revision": "적용 순서와 우선순위 규칙을 명확히 정의합니다. [확인 필요: 목록 순서와 우선순위 문장의 관계]",
      "verification_question": "'캠페인 제외'는 할인 계산 전에 확인하는 조건입니까, 아니면 계산 단계 중 하나입니까? 목록 순서와 우선순위 문장이 모순되지 않습니까?"
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
      "decision": "의미 확인 필요",
      "reader_must_infer": "'차단을 항상 우선' 규칙과 목록 내 '허용' 조건 간의 논리적 관계",
      "suggested_revision": "차단 및 허용 정책의 우선순위 규칙을 명시합니다. [확인 필요: 차단 우선 규칙과 허용 조건의 공존 여부]",
      "verification_question": "'차단을 항상 우선' 규칙이 목록의 허용 조건 (사용자, 채널) 보다 항상 적용됩니까? 아니면 예외가 있습니까?"
    },
    {
      "id": "DEV-N01",
      "decision": "구체화 필요",
      "reader_must_infer": "문장의 주체 (시스템/사용자) 및 금지/필수 동작의 서술어",
      "suggested_revision": "월말 마감 이후에는 전표를 수정할 수 없으며, 오류 전표는 취소한 후 재작성해야 합니다.",
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
