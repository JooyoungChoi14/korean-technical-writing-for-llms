{
  "cases": [
    {
      "id": "TUNE-01",
      "decision": "구체화 필요",
      "suggested_revision": "각 기관의 권한 설정을 합친다.",
      "reason": "문맥에서 정의된 한국어 용어 (기관, 권한 설정) 를 사용하지 않고 영어 명사와 콩글리시 동사 (머지한다) 를 사용하여 가독성이 떨어진다."
    },
    {
      "id": "TUNE-02",
      "decision": "구체화 필요",
      "suggested_revision": "실패한 주문에 대한 재처리 이벤트를 발행한다.",
      "reason": "재처리 레일에 올린다는 비유가 실제 동작 (Kafka 이벤트 발행) 을 가려 독자가 구현 방식을 추측하게 한다."
    },
    {
      "id": "TUNE-03",
      "decision": "구체화 필요",
      "suggested_revision": "검증을 먼저 수행하고 모두 유효할 때만 저장한다.",
      "reason": "주어와 서술어가 생략된 명사 나열로, 작업의 순서와 조건 관계를 독자가 복원해야 한다."
    },
    {
      "id": "TUNE-04",
      "decision": "구체화 필요",
      "suggested_revision": "이 분기는 응답하지 않은 문항을 평균 계산에서 제외한다.",
      "reason": "통계 왜곡을 막는다라는 평가가 실제 동작 (응답 없는 문항 제외) 을 대신하여 구체적인 처리 기준이 불명확하다."
    },
    {
      "id": "TUNE-05",
      "decision": "구체화 필요",
      "suggested_revision": "정산 대조 작업이 차이 내역을 예외 목록에 등록한다.",
      "reason": "클로즈한다는 표현이 차이 해결을 암시하나 문맥상 담당자 확인을 위한 목록 등록이므로 의미 충실도가 떨어진다."
    },
    {
      "id": "TUNE-06",
      "decision": "구체화 필요",
      "suggested_revision": "서버 기동 시 캐시를 사전 적재하는 것이 성능상 이득이다.",
      "reason": "데워두는 비유와 이득이라는 평가보다 기술 용어 (사전 적재) 와 구체적 효과 (성능) 를 명시하는 것이 명확하다."
    },
    {
      "id": "TUNE-07",
      "decision": "구체화 필요",
      "suggested_revision": "승인 규칙 집합을 계산해 사용자별 최종 승인 한도를 저장한다.",
      "reason": "문맥에 정의된 한국어 의미 (승인 규칙, 최종 승인 한도) 대신 영어 용어 나열로 되어 있어 이해에 추가 비용이 든다."
    },
    {
      "id": "TUNE-08",
      "decision": "구체화 필요",
      "suggested_revision": "권한 변경 이벤트를 감사용 Kafka 토픽에 발행한다.",
      "reason": "감사 스트림에 흘린다는 비유가 실제 동작 (Kafka 토픽 발행) 을 불명확하게 만든다."
    },
    {
      "id": "TUNE-09",
      "decision": "구체화 필요",
      "suggested_revision": "기존 API 는 유지하면서 선택 필드를 추가한다.",
      "reason": "명사 나열로 되어 있어 주체와 동작 관계가 생략되었으며 선택 적용의 의미가 모호하다."
    },
    {
      "id": "TUNE-10",
      "decision": "구체화 필요",
      "suggested_revision": "소급 수정은 마감 당시 잔액 추적을 불가능하게 한다.",
      "reason": "원장을 오염시킨다는 평가가 기술적 결과 (감사 추적 불가) 를 대신하여 구체적인 위험을 설명하지 않는다."
    },
    {
      "id": "TUNE-11",
      "decision": "구체화 필요",
      "suggested_revision": "예측 모델이 이탈 확률을 계산하고 임계값 이상인 경우 목록에 추가한다.",
      "reason": "스코어링, 어플라이한다 등 영어 동사 혼합이 실제 동작 (확률 계산, 목록 추가) 을 가린다."
    },
    {
      "id": "TUNE-12",
      "decision": "구체화 필요",
      "suggested_revision": "두 권한을 하나로 합치면 구현은 단순해지지만 보안 위험이 있다.",
      "reason": "한 바구니, 싸다 등의 비유와 평가가 기술적 trade-off(구현 단순성 대 보안 위험) 를 정확히 전달하지 못한다."
    },
    {
      "id": "TUNE-CTL-01",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "코드 식별자와 기술적 조건 (저장소, 만료 시간) 이 명확하게 명시되어 있다."
    },
    {
      "id": "TUNE-CTL-02",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "표준 용어를 사용하여 대상, 조건, 결과가 명확하게 기술되어 있다."
    },
    {
      "id": "TUNE-CTL-03",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체, 시점, 비교 대상, 조건, 동작이 모두 명시되어 의미 전달이 명확하다."
    }
  ]
}
