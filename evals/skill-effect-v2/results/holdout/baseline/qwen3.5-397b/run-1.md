{
  "cases": [
    {
      "id": "H-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "'관문'이 구체적으로 어떤 기술 컴포넌트 (파이프라인, 프록시, API 등) 인지",
      "suggested_revision": "감사 로그를 외부 분석기로 전송하는 연동 설정을 합니다.",
      "verification_question": "'관문'이 구체적으로 어떤 기술 컴포넌트나 설정을 의미합니까?"
    },
    {
      "id": "H-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "'쿠션'이 재고량, 시간 여유, 예산 중 무엇인지",
      "suggested_revision": "재고 부족 상황에 대비하여 안전 재고를 확보합니다.",
      "verification_question": "'쿠션'이 안전 재고인지 생산 여유 시간인지 명확합니까?"
    },
    {
      "id": "H-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "'소켓'이 UI 영역인지 데이터 연동接口인지",
      "suggested_revision": "모델 판정값을 업무 화면에 표시할 수 있도록 연동합니다.",
      "verification_question": "'소켓'이 UI 컴포넌트인지 데이터 연동 수단인지 명확합니까?"
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
      "reader_must_infer": "주체와 서술어가 생략되어 절차인지 상태인지 불명확함",
      "suggested_revision": "결측치를 대치한 후 회귀 모델을 재학습하며, 기존 계수는 폐기합니다.",
      "verification_question": "이 문장이 수행 절차인지 현재 상태 설명인지 명확합니까?"
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
