```json
{
  "cases": [
    {
      "id": "H-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "관문이 수행하는 실제 동작(전달, 중계, 필터링 등)",
      "suggested_revision": "감사 로그를 외부 분석기로 전달하는 중계 지점을 설정합니다.",
      "verification_question": "이 관문이 로그를 단순 전달만 하는지, 형식 변환이나 필터링도 수행하는지?"
    },
    {
      "id": "H-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "쿠션이 지칭하는 실제 개념(안전재고, 여유분, 버퍼 등)",
      "suggested_revision": "재고 부족 상황을 커버할 수 있는 안전 재고(버퍼)를 확보해야 합니다.",
      "verification_question": "쿠션이 물리적 안전 재고를 의미하는지, 아니면 주문 여유 시간 등 다른 개념인지?"
    },
    {
      "id": "H-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "소켓이 지칭하는 실제 기술 요소(API, 인터페이스, 연동 모듈 등)",
      "suggested_revision": "업무 화면에서 모델 판정값을 표시할 수 있도록 인터페이스를 제공합니다.",
      "verification_question": "소켓이 구체적으로 API 엔드포인트, UI 컴포넌트 연동 지점, 아니면 다른 기술 요소를 의미하는지?"
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
      "reader_must_infer": "주어와 서술어가 생략되어 누가/무엇이 동작을 수행하는지",
      "suggested_revision": "결측치를 대치한 뒤 회귀 모델을 재학습하며, 기존 계수는 폐기합니다.",
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
```
