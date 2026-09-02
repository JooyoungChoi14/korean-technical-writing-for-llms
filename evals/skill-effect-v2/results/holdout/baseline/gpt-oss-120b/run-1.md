```json
{
  "cases": [
    {
      "id": "H-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "‘관문’이 어떤 구성 요소이며, 누가 동작을 수행하는지 명시가 필요합니다.",
      "suggested_revision": "감사 로그를 외부 분석기로 전송하는 인터페이스를 제공합니다.",
      "verification_question": null
    },
    {
      "id": "H-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "‘쿠션’이 구체적으로 어떤 역할·구조를 갖는지 명시가 필요합니다.",
      "suggested_revision": "재고 부족을 보완하기 위한 버퍼가 필요합니다.",
      "verification_question": null
    },
    {
      "id": "H-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "‘소켓’이 실제 어떤 인터페이스·연결 방식을 의미하는지 명시가 필요합니다.",
      "suggested_revision": "모델 판정값을 업무 화면에 전달할 인터페이스를 엽니다.",
      "verification_question": null
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
      "reader_must_infer": "‘비공개를 우선한다’는 적용 규칙이 구체적으로 어떻게 동작하는지 명시가 필요합니다.",
      "suggested_revision": "현장 관리자는 공개, 본사는 보안 비공개, 문서 소유자는 공개, 기본은 비공개 순으로 적용하며, 비공개 결과가 발생하면 이를 우선 적용합니다.",
      "verification_question": null
    },
    {
      "id": "H-C02",
      "decision": "구체화 필요",
      "reader_must_infer": "‘보류를 승인보다 우선한다’는 상황·조건을 명시가 필요합니다.",
      "suggested_revision": "긴급 출고 승인, 품질 보류, 영업 승인, 기본 거절 순으로 적용하고, 품질 보류가 있을 경우 승인보다 우선 적용합니다.",
      "verification_question": null
    },
    {
      "id": "H-C03",
      "decision": "구체화 필요",
      "reader_must_infer": "‘제외를 동의보다 우선한다’는 상황·조건을 명시가 필요합니다.",
      "suggested_revision": "환자 직접 동의, 연구 제외 등록, 기관 동의, 기본 제외 순으로 판단하며, 제외가 발생하면 동의보다 우선 적용합니다.",
      "verification_question": null
    },
    {
      "id": "H-N01",
      "decision": "구체화 필요",
      "reader_must_infer": "작업 수행 주체와 시점(결측치 대치 후 언제 재학습·폐기하는지)이 명시가 필요합니다.",
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
