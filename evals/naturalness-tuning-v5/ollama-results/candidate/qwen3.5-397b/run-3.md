{
  "cases": [
    {
      "id": "TUNE-01",
      "decision": "구체화 필요",
      "suggested_revision": "권한 서비스가 기관별 권한 설정과 공통 역할 설정에 포함된 허용 메뉴를 합친다.",
      "reason": "주체 (권한 서비스) 와 병합의 실제 대상 (허용 메뉴) 이 생략되어 독자가 문맥을 찾아야 함. 영어 용어는 문맥에 정의되었으나 동작 설명이 압축됨."
    },
    {
      "id": "TUNE-02",
      "decision": "구체화 필요",
      "suggested_revision": "주문 서비스는 실패한 주문에 대한 재시도 이벤트를 Kafka 토픽에 발행한다.",
      "reason": "'레일에 올린다'는 비유가 실제 동작 (이벤트 발행) 을 가림. 주체와 매커니즘이 명확하지 않음."
    },
    {
      "id": "TUNE-03",
      "decision": "구체화 필요",
      "suggested_revision": "모든 행의 검증을 먼저 수행하고, 유효할 때만 데이터를 저장한다.",
      "reason": "주서술어가 없어 문장 자체가 정보 전달이 안 됨. 조건 (모든 행 유효시) 이 생략됨."
    },
    {
      "id": "TUNE-04",
      "decision": "구체화 필요",
      "suggested_revision": "이 조건문은 응답 없거나 이탈한 문항을 평균 계산에서 제외한다.",
      "reason": "'통계 왜곡'이라는 평가가 실제 동작 (제외) 을 대신함."
    },
    {
      "id": "TUNE-05",
      "decision": "의미 확인 필요",
      "suggested_revision": "정산 비교 작업은 차이 내역을 예외 목록에 등록해 담당자가 확인하게 한다.",
      "reason": "'클로즈한다'는 자동 완료를 암시하나 문맥상 수동 확인이 필요함. 의미 보존 위반 소지."
    },
    {
      "id": "TUNE-06",
      "decision": "구체화 필요",
      "suggested_revision": "배포 직후 지연 시간 감소를 위해 서버 기동 시 데이터를 사전 적재한다.",
      "reason": "'데워두는'비유와'이득'평가가 구체적인 트레이드오프 (메모리 vs 응답 속도) 를 가림."
    },
    {
      "id": "TUNE-07",
      "decision": "구체화 필요",
      "suggested_revision": "권한 서비스는 세 규칙을 계산해 사용자별 최종 승인 한도를 저장한다.",
      "reason": "'materialize'라는 용어가 계산 및 저장이라는 구체적 동작을 모호하게 함."
    },
    {
      "id": "TUNE-08",
      "decision": "구체화 필요",
      "suggested_revision": "권한 서비스는 역할 변경 이벤트를 감사용 Kafka 토픽에 발행한다.",
      "reason": "'흘린다'는 비유가 이벤트 발행이라는 실제 동작을 가림."
    },
    {
      "id": "TUNE-09",
      "decision": "구체화 필요",
      "suggested_revision": "기존 API 와 필드는 유지하면서 신규 필드는 선택적으로 추가한다.",
      "reason": "주서술어가 없어 동작과 조건이 명확하지 않음."
    },
    {
      "id": "TUNE-10",
      "decision": "구체화 필요",
      "suggested_revision": "마감된 분개를 수정하면 당시 잔액과 정정 내역을 추적할 수 없다.",
      "reason": "'오염시킨다'는 평가가 추적 불가능하다는 실제 문제를 대신함."
    },
    {
      "id": "TUNE-11",
      "decision": "의미 확인 필요",
      "suggested_revision": "예측 모델은 고객별 이탈 확률을 계산하고 임계값 이상인 경우 목록에 추가한다.",
      "reason": "'세그먼트 스코어링'은 고객별 계산이라는 문맥과 다를 수 있으며, '어플라이한다'는 한국어 기술 용어로 부적절함."
    },
    {
      "id": "TUNE-12",
      "decision": "의미 확인 필요",
      "suggested_revision": "권한을 통합하면 구현은 단순해지지만 조직 이동 시 이전 데이터 접근 위험이 있다.",
      "reason": "'싸다'는 평가가 구현 단순성과 보안 위험이라는 Trade-off 를 가림. 문맥상 채택하지 않은 방안임."
    },
    {
      "id": "TUNE-CTL-01",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "대상, 형식, 저장소, 기간이 모두 명확함."
    },
    {
      "id": "TUNE-CTL-02",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체, 조건, 결과가 문장 자체로 명확함."
    },
    {
      "id": "TUNE-CTL-03",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체, 시점, 조건, 동작이 모두 명시되어 추론이 불필요함."
    }
  ]
}
