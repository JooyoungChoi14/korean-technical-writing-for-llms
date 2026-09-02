```json
{
  "cases": [
    {
      "id": "H-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "'관문'이 구체적으로 어떤 구성 요소(게이트웨이, 중계 모듈, 전달 지점 등)인지",
      "suggested_revision": "감사 로그를 외부 분석기로 전달하는 게이트웨이를 배치합니다",
      "verification_question": null
    },
    {
      "id": "H-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "'쿠션'이 구체적으로 어떤 재고 전략(안전 재고, 버퍼, 예비 물량 등)인지",
      "suggested_revision": "재고 부족을 흡수할 안전 재고가 필요합니다",
      "verification_question": null
    },
    {
      "id": "H-A03",
      "decision": "의미 확인 필요",
      "reader_must_infer": "'소켓'이 네트워크 소켓, API 엔드포인트, UI 연결 지점 중 무엇인지, '꽂는다'는 어떤 동작(연결, 표시, 전달)을 의미하는지",
      "suggested_revision": null,
      "verification_question": "'소켓'은 WebSocket, API 엔드포인트, UI 컴포넌트 연결 지점 중 무엇을 의미하며, '꽂는다'는 구체적으로 어떤 동작(표시, 연결, 전송)을 의미합니까?"
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
      "decision": "구체화 필요",
      "reader_must_infer": "'비공개를 우선'이 값의 우선순위인지 규칙 적용 순서인지, 그리고 어떤 상황에서 우선하는지",
      "suggested_revision": "현장 관리자에게는 공개, 본사 보안에게는 비공개, 문서 소유자에게는 공개, 기본값은 비공개로 하며, 공개와 비공개가 충돌할 때 비공개를 우선합니다",
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
      "reader_must_infer": "동작의 주체와 서술어(무엇이 재학습하고 무엇이 폐기하는지)",
      "suggested_revision": "결측치를 대치한 뒤 회귀 모델을 재학습하고 기존 계수를 폐기합니다",
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
