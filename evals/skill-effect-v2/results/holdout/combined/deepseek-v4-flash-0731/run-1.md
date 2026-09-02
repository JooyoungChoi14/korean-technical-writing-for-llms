{
  "cases": [
    {
      "id": "H-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "관문이 구체적으로 무엇을 의미하는지(API, 파일 전송, 메시지 큐 등)와 전송 동작의 주체",
      "suggested_revision": "감사 로그를 외부 분석기로 전송하는 기능을 추가합니다.",
      "verification_question": "전송 방식(API, 파일, 메시지)은 무엇입니까?"
    },
    {
      "id": "H-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "쿠션이 구체적으로 무엇을 의미하는지(안전 재고, 대기 주문, 대체 공급 등)와 부족을 흡수하는 동작",
      "suggested_revision": "재고 부족에 대비한 안전 재고를 설정합니다.",
      "verification_question": "쿠션이 구체적으로 무엇을 의미하는가? (안전 재고, 대기 주문, 대체 공급?)"
    },
    {
      "id": "H-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "소켓이 구체적으로 무엇을 의미하는지(API, 인터페이스, DB 연결 등)와 값을 꽂는 동작의 방향",
      "suggested_revision": "업무 화면이 모델 판정값을 조회할 수 있는 인터페이스를 제공합니다.",
      "verification_question": "화면이 값을 가져오는 방식(API, DB 직접 조회)은 무엇입니까?"
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
      "reader_must_infer": "순서대로 적용한 결과와 '비공개를 우선' 규칙이 충돌할 때 어떤 결과를 선택해야 하는지",
      "suggested_revision": "비공개를 우선하되, 순서와 우선 규칙이 충돌하는 경우를 명확히 정의합니다.",
      "verification_question": "순서대로 적용한 결과와 비공개 우선이 다를 때 어떤 결과를 선택합니까?"
    },
    {
      "id": "H-C02",
      "decision": "의미 확인 필요",
      "reader_must_infer": "순서대로 적용한 결과와 '보류를 승인보다 우선' 규칙이 충돌할 때 어떤 결과를 선택해야 하는지",
      "suggested_revision": "보류를 승인보다 우선하되, 순서와 우선 규칙이 충돌하는 경우를 명확히 정의합니다.",
      "verification_question": "순서대로 적용한 결과와 보류 우선이 다를 때 어떤 결과를 선택합니까?"
    },
    {
      "id": "H-C03",
      "decision": "의미 확인 필요",
      "reader_must_infer": "순서대로 적용한 결과와 '제외를 동의보다 우선' 규칙이 충돌할 때 어떤 결과를 선택해야 하는지",
      "suggested_revision": "제외를 동의보다 우선하되, 순서와 우선 규칙이 충돌하는 경우를 명확히 정의합니다.",
      "verification_question": "순서대로 적용한 결과와 제외 우선이 다를 때 어떤 결과를 선택합니까?"
    },
    {
      "id": "H-N01",
      "decision": "구체화 필요",
      "reader_must_infer": "주체(누가 재학습하고 폐기하는지)와 동작의 대상(회귀 모델, 계수)",
      "suggested_revision": "결측치를 대치한 후 회귀 모델을 재학습하고 기존 계수를 폐기합니다.",
      "verification_question": "이 작업을 수행하는 주체(파이프라인, 담당자)는 무엇입니까?"
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
