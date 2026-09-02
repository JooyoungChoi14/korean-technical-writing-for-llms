```json
{
  "cases": [
    {
      "id": "H-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "관문이 실제로 어떤 구성 요소인지(프록시, 전달 규칙, 로그 수집기 등)",
      "suggested_revision": "감사 로그를 외부 분석기로 전달하는 중계 구성 요소를 둡니다.",
      "verification_question": "관문은 구체적으로 어떤 구성 요소입니까?(프록시, 전달 규칙, 로그 수집기 등)"
    },
    {
      "id": "H-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "쿠션이 실제로 무엇인지(안전 재고, 버퍼 수량, 임시 조달 등)",
      "suggested_revision": "재고 부족을 보완할 안전 재고가 필요합니다.",
      "verification_question": "쿠션은 안전 재고인지, 버퍼 수량인지, 또는 다른 수단입니까?"
    },
    {
      "id": "H-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "소켓과 꽂다가 실제로 어떤 동작인지(데이터 바인딩, API 엔드포인트 추가, UI 슬롯 등)",
      "suggested_revision": "모델 판정값을 업무 화면에 전달하는 데이터 연결을 추가합니다.",
      "verification_question": "소켓은 데이터 바인딩인지, API 엔드포인트인지, UI 슬롯인지?"
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
      "decision": "구체화 필요",
      "reader_must_infer": "비율의 분자가 무엇인지",
      "suggested_revision": null,
      "verification_question": "지역별 비율의 분자는 무엇입니까?"
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
      "reader_must_infer": "주체와 서술어가 빠져 있어 무엇이 결측치를 대치하고 회귀를 재학습하며 기존 계수를 폐기하는지",
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
```
