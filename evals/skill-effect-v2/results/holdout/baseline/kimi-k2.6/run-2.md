```json
{
  "cases": [
    {
      "id": "H-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "관문이 구체적으로 어떤 구성 요소(게이트웨이, 중계 서버, 전달 경로 등)인지",
      "suggested_revision": "감사 로그를 외부 분석기로 전달하는 게이트웨이를 구성합니다.",
      "verification_question": null
    },
    {
      "id": "H-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "쿠션이 구체적으로 어떤 개념(안전 재고, 완충 재고, 여유분 등)인지",
      "suggested_revision": "재고 부족을 흡수할 안전 재고가 필요합니다.",
      "verification_question": null
    },
    {
      "id": "H-A03",
      "decision": "의미 확인 필요",
      "reader_must_infer": "소켓을 열다가 실제로 어떤 동작(API 추가, 인터페이스 제공, 데이터 연동 등)을 의미하는지",
      "suggested_revision": null,
      "verification_question": "모델 판정값을 업무 화면에 제공하는 구체적인 방법은 무엇인가요? (예: API 엔드포인트 추가, 웹소켓 연결, UI 바인딩 등)"
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
      "reader_must_infer": "비율 계산의 분자가 무엇인지",
      "suggested_revision": "지역별 비율은 해당 지역의 유효 응답 수를 분모로, 전체 응답 수를 분자로 계산합니다.",
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
      "reader_must_infer": "누가(또는 어떤 프로세스가) 결측치를 대치하고 재학습하며 계수를 폐기하는지",
      "suggested_revision": "결측치를 대치한 뒤 회귀 모델을 재학습하고 기존 계수를 폐기합니다.",
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
