```json
{
  "cases": [
    {
      "id": "H-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "“관문”이 실제로 어떤 구성 요소인지(필터, 게이트웨이, 포워딩 파이프라인 등), 감사 로그를 어떤 방식으로 외부 분석기로 전달하는지",
      "suggested_revision": "감사 로그를 외부 분석기로 전송하는 중계 구성 요소를 추가합니다.",
      "verification_question": "“관문”은 감사 로그를 필터링하는 구성 요소인지, 단순히 전달하는 포워딩 파이프라인인지, 접근을 제어하는 게이트웨이인지?"
    },
    {
      "id": "H-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "“쿠션”이 실제로 무엇인지(안전 재고, 버퍼, 임시 할당량 등), “흡수”가 어떤 동작인지",
      "suggested_revision": "재고 부족을 보완할 안전 재고가 필요합니다.",
      "verification_question": "“쿠션”은 안전 재고인지, 주문 버퍼인지, 다른 재고 완충 수단인지?"
    },
    {
      "id": "H-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "“소켓”이 실제로 무엇인지(API 엔드포인트, UI 컴포넌트 슬롯, 데이터 바인딩 지점 등), “꽂다”가 어떤 동작인지",
      "suggested_revision": "모델 판정값을 업무 화면에 전달하는 인터페이스를 추가합니다.",
      "verification_question": "“소켓”은 API 엔드포인트인지, UI 컴포넌트 슬롯인지, 데이터 바인딩 지점인지?"
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
      "reader_must_infer": "비율의 분자가 무엇인지(특정 응답 유형의 수, 전체 응답 수 등)",
      "suggested_revision": null,
      "verification_question": "지역별 비율의 분자는 무엇입니까? 예를 들어 특정 응답 유형의 수인지, 전체 응답 수인지, 다른 값인지?"
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
      "reader_must_infer": "주체가 무엇인지, “기존 계수 폐기”가 재학습의 일부인지 별도 단계인지",
      "suggested_revision": "결측치를 대치한 후 회귀 모델을 재학습하고 기존 계수는 폐기합니다.",
      "verification_question": "“기존 계수 폐기”는 재학습 과정에 포함되는 동작인지 별도의 단계인지?"
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
