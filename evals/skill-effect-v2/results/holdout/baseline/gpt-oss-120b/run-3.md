```json
{
  "cases": [
    {
      "id": "H-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "‘관문’이 구체적으로 어떤 형태이며 어떻게 로그를 전송하는가",
      "suggested_revision": "감사 로그를 외부 분석기로 전송하는 인터페이스(게이트웨이)를 제공합니다.",
      "verification_question": null
    },
    {
      "id": "H-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "‘쿠션’이 구체적으로 어떤 메커니즘인지",
      "suggested_revision": "재고 부족을 보완하기 위한 안전 재고(버퍼)를 도입해야 합니다.",
      "verification_question": null
    },
    {
      "id": "H-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "‘소켓’이 구체적으로 어떤 인터페이스인지",
      "suggested_revision": "모델 판정값을 업무 화면에 전달할 수 있도록 API 엔드포인트를 개설합니다.",
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
      "decision": "의미 확인 필요",
      "reader_must_infer": "비율의 분자는 무엇을 의미하는가 (예: 전체 응답 수, 특정 항목 응답 수 등)",
      "suggested_revision": null,
      "verification_question": "비율의 분자는 무엇을 의미합니까?"
    },
    {
      "id": "H-C01",
      "decision": "구체화 필요",
      "reader_must_infer": "우선 적용 규칙이 구체적으로 어떻게 동작하는가",
      "suggested_revision": "접근 권한은 다음 순서로 적용됩니다: 1) 현장 관리자 – 공개, 2) 본사 보안 – 비공개, 3) 문서 소유자 – 공개, 4) 기본 – 비공개. 이 중 비공개 설정이 우선 적용됩니다.",
      "verification_question": null
    },
    {
      "id": "H-C02",
      "decision": "구체화 필요",
      "reader_must_infer": "각 단계가 구체적으로 어떤 의미이며 보류가 승인보다 우선하는 로직",
      "suggested_revision": "출고 승인 판단은 다음 순서로 적용됩니다: 1) 긴급 출고 – 승인, 2) 품질 보류 – 보류, 3) 영업 승인 – 승인, 4) 기본 – 거절. 보류 상태가 승인보다 우선합니다.",
      "verification_question": null
    },
    {
      "id": "H-C03",
      "decision": "구체화 필요",
      "reader_must_infer": "각 단계가 구체적으로 어떤 의미이며 제외가 동의보다 우선하는 로직",
      "suggested_revision": "환자 동의 판단은 다음 순서로 적용됩니다: 1) 환자 직접 동의 – 동의, 2) 연구 제외 등록 – 제외, 3) 기관 동의 – 동의, 4) 기본 – 제외. 제외 상태가 동의보다 우선합니다.",
      "verification_question": null
    },
    {
      "id": "H-N01",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
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
