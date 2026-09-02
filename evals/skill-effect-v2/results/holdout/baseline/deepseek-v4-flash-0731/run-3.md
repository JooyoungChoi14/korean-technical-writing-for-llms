{
  "cases": [
    {
      "id": "H-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "관문이 구체적으로 무엇을 의미하는지 (예: API, 전송 모듈, 파이프라인)",
      "suggested_revision": "감사 로그를 외부 분석기로 전송하는 경로를 추가합니다.",
      "verification_question": null
    },
    {
      "id": "H-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "쿠션이 구체적으로 무엇을 의미하는지 (예: 안전 재고, 예비 재고, 대체 공급처)",
      "suggested_revision": "재고 부족에 대비한 안전 재고가 필요합니다.",
      "verification_question": null
    },
    {
      "id": "H-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "소켓이 구체적으로 무엇을 의미하는지 (예: API, 데이터 구조, 이벤트)",
      "suggested_revision": "모델 판정값을 업무 화면에 전달하는 인터페이스를 추가합니다.",
      "verification_question": null
    },
    {
      "id": "H-P01",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "H-P02",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "H-P03",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "H-C01",
      "decision": "의미 확인 필요",
      "reader_must_infer": "비공개를 우선한다는 것의 정확한 의미 (모든 비공개 규칙이 공개 규칙보다 우선하는지, 아니면 순서에 따라 마지막 규칙이 적용되는지)",
      "suggested_revision": null,
      "verification_question": "비공개를 우선한다는 것이 모든 비공개 규칙이 공개 규칙보다 우선한다는 뜻인지, 아니면 순서상 나중에 나오는 비공개 규칙이 앞선 공개 규칙을 덮어쓴다는 뜻인지 확인이 필요합니다."
    },
    {
      "id": "H-C02",
      "decision": "의미 확인 필요",
      "reader_must_infer": "보류를 승인보다 우선한다는 것의 정확한 의미",
      "suggested_revision": null,
      "verification_question": "보류를 승인보다 우선한다는 것이 모든 보류 규칙이 승인 규칙보다 우선한다는 뜻인지, 아니면 순서상 나중에 나오는 보류 규칙이 앞선 승인 규칙을 덮어쓴다는 뜻인지 확인이 필요합니다."
    },
    {
      "id": "H-C03",
      "decision": "의미 확인 필요",
      "reader_must_infer": "제외를 동의보다 우선한다는 것의 정확한 의미",
      "suggested_revision": null,
      "verification_question": "제외를 동의보다 우선한다는 것이 모든 제외 규칙이 동의 규칙보다 우선한다는 뜻인지, 아니면 순서상 나중에 나오는 제외 규칙이 앞선 동의 규칙을 덮어쓴다는 뜻인지 확인이 필요합니다."
    },
    {
      "id": "H-N01",
      "decision": "구체화 필요",
      "reader_must_infer": "주체와 동작의 연결 (누가, 언제)",
      "suggested_revision": "결측치를 대치한 후 회귀 모델을 재학습하고 기존 계수를 폐기합니다.",
      "verification_question": null
    },
    {
      "id": "H-P04",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "H-P05",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    }
  ]
}
