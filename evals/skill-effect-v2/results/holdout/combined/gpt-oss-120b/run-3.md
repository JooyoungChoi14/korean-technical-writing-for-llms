```json
{
  "cases": [
    {
      "id": "H-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "‘관문’이 구체적으로 어떤 구현(예: API 엔드포인트, 모듈)인지",
      "suggested_revision": "감사 로그를 외부 분석기로 전송하는 인터페이스(게이트웨이)를 제공합니다.",
      "verification_question": "‘관문’이 실제로 어떤 형태로 구현되는지 확인이 필요합니다."
    },
    {
      "id": "H-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "‘쿠션’이 구체적으로 어떤 메커니즘(예: 안전 재고, 버퍼)인지",
      "suggested_revision": "재고 부족을 보완할 안전 재고(버퍼)가 필요합니다.",
      "verification_question": null
    },
    {
      "id": "H-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "‘소켓’이 어떤 통신 방식(예: WebSocket, API)인지",
      "suggested_revision": "모델 판정값을 업무 화면에 전달하기 위한 API 엔드포인트를 엽니다.",
      "verification_question": "‘소켓’이 구체적으로 어떤 형태의 인터페이스인지 확인이 필요합니다."
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
      "reader_must_infer": "비율을 계산할 때 사용되는 분자는 무엇인지",
      "suggested_revision": "지역별 비율은 해당 지역의 유효 응답 수를 전체 유효 응답 수(분모)로 나누어 계산합니다.",
      "verification_question": null
    },
    {
      "id": "H-C01",
      "decision": "구체화 필요",
      "reader_must_infer": "‘비공개를 우선’한다는 구체적인 적용 규칙",
      "suggested_revision": "접근 권한은 다음 순서로 적용됩니다: 현장 관리자 – 공개, 본사 보안 – 비공개, 문서 소유자 – 공개, 기본 – 비공개. 이 중 하나라도 비공개인 경우 최종 권한은 비공개로 합니다.",
      "verification_question": null
    },
    {
      "id": "H-C02",
      "decision": "구체화 필요",
      "reader_must_infer": "보류와 승인 충돌 시 최종 결과가 무엇인지",
      "suggested_revision": "권한 판단은 긴급 출고 승인 → 품질 보류 → 영업 승인 → 기본 거절 순으로 적용합니다. 품질 보류와 승인이 동시에 적용될 경우, 보류가 우선하여 최종 결과는 보류됩니다.",
      "verification_question": null
    },
    {
      "id": "H-C03",
      "decision": "구체화 필요",
      "reader_must_infer": "제외와 동의가 동시에 적용될 때의 우선순위",
      "suggested_revision": "판정은 환자 직접 동의 → 연구 제외 등록 → 기관 동의 → 기본 제외 순으로 진행합니다. 제외와 동의가 동시에 적용될 경우, 제외가 우선하여 최종 판정은 제외됩니다.",
      "verification_question": null
    },
    {
      "id": "H-N01",
      "decision": "구체화 필요",
      "reader_must_infer": null,
      "suggested_revision": "결측치를 대치한 후 회귀 모델을 재학습하고, 이전 모델의 계수는 폐기합니다.",
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
