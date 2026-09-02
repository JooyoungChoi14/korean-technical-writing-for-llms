{
  "cases": [
    {
      "id": "H-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "'관문'이 의미하는 기술 구성 요소 (프록시, 큐 등)",
      "suggested_revision": "감사 로그를 외부 분석기로 전송하기 전에 검증하거나 중계하는 구성 요소를 설정합니다.",
      "verification_question": "'관문'이 프록시, 큐, 방화벽 규칙 중 무엇을 의미합니까?"
    },
    {
      "id": "H-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "'쿠션'의 구체적 정의 (안전 재고 수량 등)",
      "suggested_revision": "재고 부족 발생 시 대비할 수 있는 안전 재고 (Safety Stock) 가 필요합니다.",
      "verification_question": "'쿠션'이 안전 재고 수량을 의미합니까, 아니면 납기 지연 허용 기간을 의미합니까?"
    },
    {
      "id": "H-A03",
      "decision": "의미 확인 필요",
      "reader_must_infer": "'소켓'의 인터페이스 종류 및 '엽니다'의 동작 의미",
      "suggested_revision": "모델 판정값을 업무 화면에서 조회할 수 있도록 API 엔드포인트를 개방합니다.",
      "verification_question": "'소켓'이 API 인터페이스를 의미합니까, 아니면 UI 컴포넌트 삽입 지점을 의미합니까?"
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
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "H-C02",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "H-C03",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "H-N01",
      "decision": "구체화 필요",
      "reader_must_infer": "주체와 서술어 (누가 언제 하는 행위인지)",
      "suggested_revision": "결측치를 대치한 후 회귀 모델을 재학습하며, 기존 계수는 폐기합니다.",
      "verification_question": "'기존 계수 폐기'가 재학습 완료 후 즉시 이루어지는 행위입니까?"
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
