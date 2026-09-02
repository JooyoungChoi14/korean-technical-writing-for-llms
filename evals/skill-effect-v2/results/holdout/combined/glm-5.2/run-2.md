```json
{
  "cases": [
    {
      "id": "H-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "관문이 실제로 어떤 구성 요소나 메커니즘인지 (전달 단계, 필터, 프록시 등)",
      "suggested_revision": "감사 로그를 외부 분석기로 전달하는 전송 단계를 둡니다.",
      "verification_question": "관문은 단순 전달 단계인지, 필터링이나 변환이 포함된 구성 요소인지?"
    },
    {
      "id": "H-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "쿠션이 실제로 무엇인지 (안전 재고, 버퍼 수량 등), 흡수가 어떤 동작인지 (부족분 보전)",
      "suggested_revision": "재고 부족분을 보전할 안전 재고가 필요합니다.",
      "verification_question": "쿠션은 안전 재고 수량인지, 주문 조정이나 대체 조달 같은 다른 수단인지?"
    },
    {
      "id": "H-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "소켓이 실제로 어떤 인터페이스인지 (API 엔드포인트, 데이터 바인딩 등), 꽂다가 어떤 동작인지 (데이터 전달)",
      "suggested_revision": "모델 판정값을 업무 화면에 전달하는 데이터 연결을 추가합니다.",
      "verification_question": "소켓은 API 엔드포인트인지, 화면 데이터 바인딩인지, 다른 인터페이스인지?"
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
      "decision": "의미 확인 필요",
      "reader_must_infer": "비율의 분자가 무엇인지 (전체 유효 응답 수, 특정 응답 유형의 수 등)",
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
      "reader_must_infer": "주체가 무엇인지, 두 동작의 관계가 순차적 단계인지 결과인지",
      "suggested_revision": "결측치를 대치한 뒤 회귀 모델을 재학습하고 기존 계수는 폐기합니다.",
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
