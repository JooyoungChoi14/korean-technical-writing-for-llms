```json
{
  "cases": [
    {
      "id": "H-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "‘관문’이 구체적으로 어떤 구성 요소이며, 로그 전송 방식이 어떻게 구현되는지",
      "suggested_revision": "감사 로그를 외부 분석기로 전송하는 게이트웨이를 제공합니다.",
      "verification_question": null
    },
    {
      "id": "H-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "‘쿠션’이 의미하는 구체적인 메커니즘(예: 안전 재고, 버퍼)과 구현 위치",
      "suggested_revision": "재고 부족을 보완하기 위한 안전 재고(버퍼)가 필요합니다.",
      "verification_question": null
    },
    {
      "id": "H-A03",
      "decision": "의미 확인 필요",
      "reader_must_infer": "‘소켓’이 의미하는 구체적인 구현체와 이를 여는 주체",
      "suggested_revision": null,
      "verification_question": "‘소켓’이 의미하는 구체적인 구현체(예: API 엔드포인트, WebSocket 등)와 이를 여는 주체는 누구입니까?"
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
      "reader_must_infer": "‘비공개’를 우선 적용한다는 규칙이 어떤 상황에서 적용되는지 구체적인 설명 필요",
      "suggested_revision": "어떤 규칙이라도 비공개로 결정되면, 공개 규칙보다 우선 적용됩니다.",
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
      "reader_must_infer": "‘결측치 대치 후 회귀 재학습, 기존 계수 폐기’가 수행되는 주체와 시점",
      "suggested_revision": "결측치를 대치한 후 회귀 모델을 재학습하고, 기존 회귀 계수를 폐기합니다.",
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
