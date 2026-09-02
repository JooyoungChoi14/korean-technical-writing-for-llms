```json
{
  "cases": [
    {
      "id": "H-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "‘관문’이 구체적으로 어떤 역할을 하는지(전송 메커니즘)",
      "suggested_revision": "감사 로그를 외부 분석기로 전송하는 인터페이스(게이트웨이)를 제공합니다.",
      "verification_question": null
    },
    {
      "id": "H-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "‘쿠션’이 의미하는 구체적인 메커니즘(재고 버퍼)",
      "suggested_revision": "재고 부족 상황을 완화하기 위한 재고 버퍼가 필요합니다.",
      "verification_question": null
    },
    {
      "id": "H-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "‘소켓’이 의미하는 구체적인 인터페이스(예: API)",
      "suggested_revision": "모델 판정값을 업무 화면에 전달하기 위한 API 엔드포인트를 제공합니다.",
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
      "decision": "구체화 필요",
      "reader_must_infer": "‘비율’이 무엇을 나타내는지(전체 대비 비율)",
      "suggested_revision": "지역별 비율은 해당 지역의 유효 응답 수를 전체 유효 응답 수(분모)로 나누어 계산합니다.",
      "verification_question": null
    },
    {
      "id": "H-C01",
      "decision": "구체화 필요",
      "reader_must_infer": "‘비공개를 우선’이 의미하는 적용 우선순위",
      "suggested_revision": "접근 권한은 다음 순서로 적용합니다: 1) 현장 관리자 – 공개, 2) 본사 보안 – 비공개, 3) 문서 소유자 – 공개, 4) 기본 – 비공개. 동일한 대상에 대해 충돌이 발생하면 비공개 규칙이 우선합니다.",
      "verification_question": null
    },
    {
      "id": "H-C02",
      "decision": "구체화 필요",
      "reader_must_infer": "보류와 승인 충돌 시 적용 규칙",
      "suggested_revision": "출고 승인 정책은 다음 순서로 적용합니다: 1) 긴급 출고 – 승인, 2) 품질 보류 – 보류, 3) 영업 승인 – 승인, 4) 기본 – 거절. 보류 상태가 존재하면 승인보다 우선적으로 적용됩니다.",
      "verification_question": null
    },
    {
      "id": "H-C03",
      "decision": "구체화 필요",
      "reader_must_infer": "‘제외’와 ‘동의’ 충돌 시 적용 규칙",
      "suggested_revision": "환자 데이터 처리 여부는 다음 순서로 판단합니다: 1) 환자 직접 동의 – 포함, 2) 연구 제외 등록 – 제외, 3) 기관 동의 – 포함, 4) 기본 – 제외. ‘제외’ 규칙이 ‘동의’ 규칙보다 우선 적용됩니다.",
      "verification_question": null
    },
    {
      "id": "H-N01",
      "decision": "구체화 필요",
      "reader_must_infer": "누가 재학습을 수행하는지(시스템)",
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
