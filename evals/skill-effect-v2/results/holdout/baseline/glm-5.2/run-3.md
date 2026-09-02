```json
{
  "cases": [
    {
      "id": "H-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "관문이 실제로 어떤 구성 요소(필터, 프록시, 전송 규칙 등)인지",
      "suggested_revision": "감사 로그를 외부 분석기로 전송하는 중계 구성 요소를 추가합니다.",
      "verification_question": "관문이 구체적으로 어떤 구성 요소(필터, 프록시, 사이드카, 포워딩 규칙 등)를 가리킵니까?"
    },
    {
      "id": "H-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "쿠션이 실제로 무엇(안전 재고, 버퍼, 임계값 조정 등)이며 흡수가 어떤 동작인지",
      "suggested_revision": "재고 부족 시 출하를 유지할 안전 재고를 둡니다.",
      "verification_question": "쿠션이 안전 재고, 버퍼, 임계값 조정 중 어느 것입니까?"
    },
    {
      "id": "H-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "소켓이 실제로 어떤 인터페이스(API 엔드포인트, UI 데이터 바인딩, 메시지 큐 등)이며 꽂다와 열다가 어떤 동작인지",
      "suggested_revision": "모델 판정값을 업무 화면에 전달하는 인터페이스를 추가합니다.",
      "verification_question": "소켓이 API 엔드포인트, UI 데이터 바인딩, 메시지 큐 중 어느 것입니까?"
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
      "reader_must_infer": "비율의 분자가 무엇인지(전체 응답 수, 특정 응답 유형 수 등)",
      "suggested_revision": "지역별 비율은 [확인 필요: 분자]를 해당 지역의 유효 응답 수로 나누어 계산합니다.",
      "verification_question": "지역별 비율의 분자는 무엇입니까?(예: 특정 응답 유형의 수, 전체 응답 수 등)"
    },
    {
      "id": "H-C01",
      "decision": "구체화 필요",
      "reader_must_infer": "적용 대상이 무엇인지, 각 규칙의 방향(누구에게 공개/비공개인지)과 적용 주체가 누구인지",
      "suggested_revision": "문서의 공개 범위는 현장 관리자에게 공개, 본사 보안 부서에 비공개, 문서 소유자에게 공개, 기본 비공개 순으로 적용하며 충돌 시 비공개를 우선합니다.",
      "verification_question": "적용 대상이 문서인지, 각 규칙이 '누구에게 공개/비공개'를 의미하는지 확인이 필요합니다."
    },
    {
      "id": "H-C02",
      "decision": "구체화 필요",
      "reader_must_infer": "적용 대상이 무엇(출고 요청, 주문 등)인지, 각 규칙의 판정 주체와 동작이 무엇인지",
      "suggested_revision": "출고 요청은 긴급 출고 승인, 품질 보류, 영업 승인, 기본 거절 순으로 판정하며 보류를 승인보다 우선합니다.",
      "verification_question": "적용 대상이 출고 요청인지, 각 규칙의 판정 주체가 누구(품질팀, 영업팀 등)인지 확인이 필요합니다."
    },
    {
      "id": "H-C03",
      "decision": "구체화 필요",
      "reader_must_infer": "판정 대상이 무엇(환자 데이터 포함 여부 등)인지, 각 규칙의 주체와 동작이 무엇인지",
      "suggested_revision": "환자 데이터 포함 여부는 환자 직접 동의, 연구 제외 등록, 기관 동의, 기본 제외 순으로 판정하며 제외를 동의보다 우선합니다.",
      "verification_question": "판정 대상이 환자 데이터 포함 여부인지, 각 규칙의 주체가 누구(환자, 연구자, 기관 등)인지 확인이 필요합니다."
    },
    {
      "id": "H-N01",
      "decision": "구체화 필요",
      "reader_must_infer": "주체가 누구인지, 기존 계수 폐기가 재학습 전인지 후인지, 대치 방법이 무엇인지",
      "suggested_revision": "결측치를 대치한 후 회귀 모델을 재학습하고 기존 계수는 폐기합니다.",
      "verification_question": "기존 계수 폐기가 재학습 전(기존 계수를 버리고 새로 학습)인지 후(재학습 후 이전 계수 삭제)인지 확인이 필요합니다."
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
