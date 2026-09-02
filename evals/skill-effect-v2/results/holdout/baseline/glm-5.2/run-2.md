```json
{
  "cases": [
    {
      "id": "H-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "관문이 실제로 어떤 구성 요소(프록시, 필터, 큐 등)이며 어떤 동작(전달, 필터링, 버퍼링 등)을 수행하는지",
      "suggested_revision": "감사 로그를 외부 분석기로 전달하는 프록시를 둡니다.",
      "verification_question": "관문은 로그를 필터링하는 구성 요소입니까, 아니면 전달만 담당하는 프록시입니까?"
    },
    {
      "id": "H-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "쿠션이 실제로 무엇(안전 재고, 버퍼, 대체 공급 등)이며 흡수가 어떤 동작(보완, 대체, 완충 등)인지",
      "suggested_revision": "재고 부족을 보완할 안전 재고가 필요합니다.",
      "verification_question": "쿠션은 안전 재고를 의미합니까, 아니면 대체 공급처나 주문 버퍼를 의미합니까?"
    },
    {
      "id": "H-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "소켓이 실제로 어떤 인터페이스(API, 데이터 바인딩, 상태 공유 등)이며 꽂는다가 어떤 동작(조회, 구독, 연결 등)인지",
      "suggested_revision": "모델 판정값을 업무 화면에서 조회할 수 있도록 API를 공개합니다.",
      "verification_question": "판정값을 화면에 전달하는 방식은 API 호출입니까, 실시간 구독입니까, 아니면 상태 공유입니까?"
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
      "reader_must_infer": "비율의 분자가 무엇인지(해당 지역의 특정 응답 수, 전체 응답 수 중 해당 지역 비중 등)",
      "suggested_revision": "지역별 비율은 해당 지역의 특정 응답 수를 분자로, 해당 지역의 유효 응답 수를 분모로 계산합니다.",
      "verification_question": "분자는 해당 지역의 특정 항목 응답 수입니까, 아니면 다른 값입니까?"
    },
    {
      "id": "H-C01",
      "decision": "구체화 필요",
      "reader_must_infer": "각 명사 나열이 조건과 결과를 압축하고 있으며, 순차 적용과 비공개 우선이 충돌할 때 어떻게 동작하는지",
      "suggested_revision": "현장 관리자는 공개, 본사 보안 담당자는 비공개, 문서 소유자는 공개, 그 외는 비공개로 설정하며, 규칙이 충돌하면 비공개를 우선합니다.",
      "verification_question": "순차 적용과 비공개 우선 중 실제로 어떤 규칙이 최종 가시성을 결정합니까?"
    },
    {
      "id": "H-C02",
      "decision": "구체화 필요",
      "reader_must_infer": "각 명사 나열이 조건과 결과를 압축하고 있으며, 순차 적용과 보류 우선이 충돌할 때 어떻게 동작하는지",
      "suggested_revision": "긴급 출고 요청은 승인, 품질 검사 결과는 보류, 영업 부서 요청은 승인, 그 외는 거절로 처리하며, 보류를 승인보다 우선합니다.",
      "verification_question": "순차 적용과 보류 우선 중 실제로 어떤 규칙이 최종 결과를 결정합니까?"
    },
    {
      "id": "H-C03",
      "decision": "구체화 필요",
      "reader_must_infer": "각 명사 나열이 조건과 결과(포함 또는 제외)를 압축하고 있으며, 순차 판정과 제외 우선이 충돌할 때 어떻게 동작하는지",
      "suggested_revision": "환자가 직접 동의한 경우는 포함, 연구 제외로 등록된 경우는 제외, 기관이 동의한 경우는 포함, 그 외는 제외로 판정하며, 제외를 동의보다 우선합니다.",
      "verification_question": "환자 직접 동의의 결과는 포함입니까, 아니면 다른 상태입니까?"
    },
    {
      "id": "H-N01",
      "decision": "구체화 필요",
      "reader_must_infer": "주체가 무엇이며, 결측치 대치·회귀 재학습·기존 계수 폐기의 순서와 관계",
      "suggested_revision": "결측치를 대치한 후 회귀 모델을 재학습하고 기존 계수는 폐기합니다.",
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
