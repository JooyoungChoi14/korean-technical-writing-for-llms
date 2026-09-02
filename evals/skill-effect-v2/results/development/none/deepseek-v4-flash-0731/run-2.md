{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "다리"가 의미하는 기술 요소(예: API, 메시지 큐, 데이터 전송 계층)",
      "suggested_revision": "정산 결과를 다음 단계로 전달하는 인터페이스(또는 파이프라인)를 구현합니다.",
      "verification_question": "다리"가 구체적으로 어떤 기술 요소를 의미하는지 확인 필요"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "완충지대"가 예외 처리 메커니즘(예: try-catch, 데드레터 큐)을 의미함",
      "suggested_revision": "예외를 처리하는 핸들러(또는 버퍼)를 추가합니다.",
      "verification_question": "완충지대"가 구체적으로 어떤 예외 처리 방식을 의미하는지 확인"
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "손잡이"가 통계 값을 화면에 전달하는 기능(예: API, 뷰)을 의미함",
      "suggested_revision": "통계 값을 화면에 표시하기 위한 조회 API(또는 핸들러)를 추가합니다.",
      "verification_question": "손잡이"가 구체적으로 어떤 기술 요소인지 확인"
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
      "reader_must_infer": "제외 조건"이 캠페인 제외만을 의미하는지, 다른 제외 조건이 있는지",
      "suggested_revision": "개별 상품 할인, 회원 등급 할인, 캠페인 제외, 기본 가격 순으로 적용하며, 캠페인 제외와 같은 제외 조건은 모든 할인보다 우선합니다.",
      "verification_question": "제외 조건"이 캠페인 제외만을 의미하는지, 다른 제외 조건이 있는지 확인 필요"
    },
    {
      "id": "DEV-C02",
      "decision": "의미 확인 필요",
      "reader_must_infer": "보류"가 자동 보류만을 의미하는지, 다른 보류 유형이 있는지",
      "suggested_revision": "수동 승인, 자동 보류, 부서 승인, 기본 거절 순으로 판정하며, 자동 보류는 수동 승인과 부서 승인보다 우선합니다.",
      "verification_question": "보류"가 자동 보류만을 지칭하는지, 다른 보류 유형이 있는지 확인"
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
