```json
{
  "cases": [
    {
      "id": "H-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "관문이 실제로 어떤 구성 요소인지(프록시, 로그 포워딩 규칙, 수집 에이전트 등)",
      "suggested_revision": "감사 로그를 외부 분석기로 전달하는 중계 구성 요소를 둡니다.",
      "verification_question": "관문은 프록시 서버, 로그 포워딩 규칙, 수집 에이전트 중 어떤 구성 요소를 가리킵니까?"
    },
    {
      "id": "H-A02",
      "decision": "의미 확인 필요",
      "reader_must_infer": "쿠션이 안전 재고, 버퍼 재고, 수요 평활 알고리즘 중 어느 것인지",
      "suggested_revision": null,
      "verification_question": "쿠션은 안전 재고량, 버퍼 재고, 수요 평활 알고리즘 중 어떤 구체적 수단을 가리킵니까?"
    },
    {
      "id": "H-A03",
      "decision": "의미 확인 필요",
      "reader_must_infer": "소켓이 API 엔드포인트, UI 데이터 바인딩, 화면 슬롯 중 어느 것인지",
      "suggested_revision": null,
      "verification_question": "소켓은 API 엔드포인트, UI 컴포넌트 슬롯, 데이터 바인딩 중 어떤 메커니즘을 가리킵니까?"
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
      "suggested_revision": "지역별 비율은 [확인 필요] 수를 해당 지역의 유효 응답 수로 나누어 계산합니다.",
      "verification_question": "비율의 분자에 해당하는 수치는 무엇입니까?"
    },
    {
      "id": "H-C01",
      "decision": "구체화 필요",
      "reader_must_infer": "공개/비공개의 대상이 무엇인지, 각 주체와 공개/비공개의 관계",
      "suggested_revision": "문서 공개 범위는 현장 관리자 지정 시 공개, 본사 보안 지정 시 비공개, 문서 소유자 지정 시 공개, 지정 없을 시 비공개 순으로 적용하며 비공개를 우선합니다.",
      "verification_question": "현장 관리자 공개는 현장 관리자가 공개로 지정한 경우를 뜻합니까?"
    },
    {
      "id": "H-C02",
      "decision": "구체화 필요",
      "reader_must_infer": "승인/보류/거절의 대상이 무엇인지, 각 조건과 결과의 관계",
      "suggested_revision": "출고 요청은 긴급 출고인 경우 승인, 품질 검사 대상인 경우 보류, 영업 부서 승인 시 승인, 해당 없을 시 거절 순으로 적용하며 보류를 승인보다 우선합니다.",
      "verification_question": "긴급 출고 승인은 긴급 출고 요청을 자동 승인한다는 뜻입니까?"
    },
    {
      "id": "H-C03",
      "decision": "구체화 필요",
      "reader_must_infer": "동의/제외의 대상이 무엇인지, 각 조건과 결과의 관계",
      "suggested_revision": "연구 참여 여부는 환자 직접 동의 시 포함, 연구 제외 등록 시 제외, 기관 동의 시 포함, 해당 없을 시 제외 순으로 판정하며 제외를 동의보다 우선합니다.",
      "verification_question": "환자 직접 동의는 환자가 직접 동의한 경우 연구에 포함한다는 뜻입니까?"
    },
    {
      "id": "H-N01",
      "decision": "구체화 필요",
      "reader_must_infer": "주체가 누구인지, 각 단계의 순서와 조건",
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
