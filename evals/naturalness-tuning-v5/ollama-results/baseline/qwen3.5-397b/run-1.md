{
  "cases": [
    {
      "id": "TUNE-01",
      "decision": "구체화 필요",
      "suggested_revision": "각 기관의 권한 설정을 합친다.",
      "reason": "영어 용어 (tenant, entitlement snapshot, 머지) 와 한국어 조사의 결합이 독자의 복원 작업을 요구한다. 문맥에 정의된 한국어 용어로 대체하고 동작을 명확히 한다."
    },
    {
      "id": "TUNE-02",
      "decision": "구체화 필요",
      "suggested_revision": "실패한 주문에 대한 재처리 이벤트를 발행한다.",
      "reason": "비유적 표현 (레일에 올린다) 이 실제 동작 (이벤트 발행) 을 가린다. 기술적 동작을 명시적으로 서술한다."
    },
    {
      "id": "TUNE-03",
      "decision": "구체화 필요",
      "suggested_revision": "모든 행의 검증을 먼저 수행하고, 유효할 경우에만 데이터를 저장한다.",
      "reason": "주체와 서술어가 생략된 명사 나열문이다. 공간이 제한된 경우에도 최소한의 서술어를 추가해 흐름을 명확히 한다."
    },
    {
      "id": "TUNE-04",
      "decision": "구체화 필요",
      "suggested_revision": "이 분기는 응답하지 않거나 값이 없는 문항을 평균 계산에서 제외한다.",
      "reason": "평가 (통계 왜곡을 막는다) 가 사실 (제외한다) 을 대신한다. 실제 조건과 동작을 명시한다."
    },
    {
      "id": "TUNE-05",
      "decision": "구체화 필요",
      "suggested_revision": "정산 대조 작업이 차이 내역을 예외 목록에 등록한다.",
      "reason": "클로즈한다라는 표현은 자동 승인을 암시할 수 있어 문맥 (담당자 확인) 과 충돌한다. 실제 동작 (목록 등록) 으로 구체화한다."
    },
    {
      "id": "TUNE-06",
      "decision": "구체화 필요",
      "suggested_revision": "서버 기동 시 데이터를 사전에 적재하는 것이 이득이다.",
      "reason": "비유적 표현 (데워두는) 을 기술 용어 (사전 적재) 로 변경해 의미를 명확히 한다."
    },
    {
      "id": "TUNE-07",
      "decision": "구체화 필요",
      "suggested_revision": "승인 규칙 조합의 최종 한도를 미리 계산해 저장한다.",
      "reason": "영어 용어 나열 (approval matrix, effective rule, materialize) 이 실제 연산 (미리 계산해 저장) 을 가린다."
    },
    {
      "id": "TUNE-08",
      "decision": "구체화 필요",
      "suggested_revision": "권한 변경 이벤트를 감사용 토픽에 발행한다.",
      "reason": "비유적 표현 (흘린다) 이 실제 동작 (이벤트 발행) 을 모호하게 만든다. 기술적 동작을 명시한다."
    },
    {
      "id": "TUNE-09",
      "decision": "구체화 필요",
      "suggested_revision": "기존 API 는 유지하면서 신규 필드는 선택적으로 적용한다.",
      "reason": "명사 나열로 관계가 압축되었다. 접속사와 서술어를 보완해 호환 방식과 적용 조건을 명확히 한다."
    },
    {
      "id": "TUNE-10",
      "decision": "구체화 필요",
      "suggested_revision": "소급 수정은 마감 당시 잔액 추적을 어렵게 만든다.",
      "reason": "평가 (오염시킨다) 가 사실 (추적 어려움) 을 대신한다. 구체적인 영향 범위를 서술한다."
    },
    {
      "id": "TUNE-11",
      "decision": "구체화 필요",
      "suggested_revision": "예측 모델이 고객별 확률을 계산하고 기준값 이상인 경우만 선별한다.",
      "reason": "영어 복합어 (세그먼트 스코어링, 컷오프 어플라이) 가 대상 (고객) 과 동작 (선별) 을 모호하게 만든다."
    },
    {
      "id": "TUNE-12",
      "decision": "구체화 필요",
      "suggested_revision": "두 권한을 통합하면 구현은 단순해지지만 보안 위험이 있다.",
      "reason": "비유 (한 바구니) 와 평가 (싸다) 가 구체적인 trade-off(구현 단순화 vs 보안 위험) 를 가린다."
    },
    {
      "id": "TUNE-CTL-01",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "식별자 형식, 저장소, 만료 시간을 모두 명시하여 독자가 추가 추론할 필요가 없다."
    },
    {
      "id": "TUNE-CTL-02",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "표준 용어를 사용하며 조건 (세 번 실패) 과 결과 (제외) 가 명확하게 서술되었다."
    },
    {
      "id": "TUNE-CTL-03",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체, 시점, 비교 대상, 조건, 동작이 모두 명시되어 의미 보존과 명확성이 확보되었다."
    }
  ]
}
