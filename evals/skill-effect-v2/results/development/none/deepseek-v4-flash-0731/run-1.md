{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "다리가 구체적으로 어떤 전송 메커니즘(예: API, 메시지 큐, 데이터 파이프라인)을 의미하는지",
      "suggested_revision": "정산 결과를 다음 단계로 전달하는 인터페이스(예: API 또는 메시지 큐)를 구현합니다.",
      "verification_question": "다리가 의미하는 기술 요소는 무엇인가?"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "완충지대가 예외를 처리하는 코드 블록, 미들웨어, 또는 재시도 로직을 의미하는지",
      "suggested_revision": "예외를 캡처하고 처리하는 중간 계층(예: try-catch 블록 또는 미들웨어)을 추가합니다.",
      "verification_question": "완충지대가 구체적으로 어떤 구현을 의미하는가?"
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "손잡이가 통계 값을 조회하여 화면에 전달하는 API 엔드포인트, 핸들러, 또는 데이터 바인딩을 의미하는지",
      "suggested_revision": "통계 값을 화면에 표시하기 위한 API 엔드포인트(또는 핸들러)를 추가합니다.",
      "verification_question": "손잡이가 구체적으로 어떤 기술 요소인가?"
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
      "reader_must_infer": "캠페인 제외가 할인 적용 순서에 포함되는지, 아니면 별도의 제외 조건인지",
      "suggested_revision": "할인 적용 순서: 개별 상품 할인, 회원 등급 할인, 기본 가격 순으로 적용하고, 캠페인 제외 조건은 할인보다 우선하여 적용합니다.",
      "verification_question": "캠페인 제외가 할인 적용 순서에 포함되는지, 아니면 별도의 우선 조건인지?"
    },
    {
      "id": "DEV-C02",
      "decision": "의미 확인 필요",
      "reader_must_infer": "보류가 자동 보류만을 의미하는지, 아니면 다른 보류 조건이 있는지",
      "suggested_revision": "판정 순서: 수동 승인, 자동 보류, 부서 승인, 기본 거절 순으로 적용하고, 보류 조건은 승인보다 우선합니다.",
      "verification_question": "보류를 승인보다 우선한다는 것이 자동 보류를 수동 승인보다 우선한다는 뜻인지?"
    },
    {
      "id": "DEV-C03",
      "decision": "의미 확인 필요",
      "reader_must_infer": "차단을 항상 우선이 구체적으로 어떤 차단 조건(조직 알림 차단, 기본 차단)을 의미하는지",
      "suggested_revision": "알림 적용 순서: 사용자 알림 허용, 채널 허용, 기본 차단 순으로 적용하고, 조직 알림 차단은 항상 우선합니다.",
      "verification_question": "조직 알림 차단이 항상 우선한다는 것이 명확한가?"
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
