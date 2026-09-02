{
  "cases": [
    {
      "id": "TUNE-01",
      "decision": "구체화 필요",
      "suggested_revision": "각 기관의 권한 설정을 합쳐 사용자별 유효 메뉴 권한으로 저장한다.",
      "reason": "영어 명사 결합과 '머지' 비유가 실제 동작 (허용 메뉴 통합) 을 가린다."
    },
    {
      "id": "TUNE-02",
      "decision": "구체화 필요",
      "suggested_revision": "실패한 주문에 대한 재시도 이벤트를 Kafka 토픽에 발행한다.",
      "reason": "'레일' 비유가 실제 동작 (이벤트 발행) 을 대체한다."
    },
    {
      "id": "TUNE-03",
      "decision": "구체화 필요",
      "suggested_revision": "모든 행의 검증을 먼저 수행하고, 유효할 경우에만 데이터를 저장한다.",
      "reason": "명사 나열이 주체와 전제 조건 (전부 유효할 때만) 을 생략한다."
    },
    {
      "id": "TUNE-04",
      "decision": "구체화 필요",
      "suggested_revision": "이 조건문은 응답하지 않음과 이탈한 문항을 평균 계산에서 제외한다.",
      "reason": "평가 ('왜곡') 가 실제 동작 (계산 제외) 을 대신한다."
    },
    {
      "id": "TUNE-05",
      "decision": "구체화 필요",
      "suggested_revision": "정산 비교 잡이 차이 내역을 예외 목록에 등록한다.",
      "reason": "'클로즈'는 해결을 암시하나 문맥상 수동 확인용으로 목록만 등록한다."
    },
    {
      "id": "TUNE-06",
      "decision": "구체화 필요",
      "suggested_revision": "서버 기동 시 자주 조회되는 데이터를 캐시에 사전 적재하는 것이 성능상 이득이다.",
      "reason": "'데워두기' 비유가 기술 동작 (사전 적재) 을 대체한다."
    },
    {
      "id": "TUNE-07",
      "decision": "구체화 필요",
      "suggested_revision": "승인 규칙 집합을 계산해 사용자별 최종 승인 한도를 저장한다.",
      "reason": "영어 용어와 'materialize'가 실제 동작 (최종 한도 계산 및 저장) 을 가린다."
    },
    {
      "id": "TUNE-08",
      "decision": "구체화 필요",
      "suggested_revision": "권한 변경 이벤트를 감사용 Kafka 토픽에 발행한다.",
      "reason": "'흘린다' 비유가 실제 동작 (이벤트 발행) 을 대체한다."
    },
    {
      "id": "TUNE-09",
      "decision": "구체화 필요",
      "suggested_revision": "기존 API 와 필드를 유지하면서 신규 필드는 선택적으로 추가한다.",
      "reason": "명사 나열이 서술어와 신규 필드 적용 방식을 생략한다."
    },
    {
      "id": "TUNE-10",
      "decision": "구체화 필요",
      "suggested_revision": "마감된 원장의 분개를 소급 수정하지 않는다.",
      "reason": "평가 ('오염') 가 실제 제약 (소급 수정 금지) 을 대신한다."
    },
    {
      "id": "TUNE-11",
      "decision": "구체화 필요",
      "suggested_revision": "예측 모델이 고객별 이탈 확률을 계산하고, 임계값 이상인 경우 목록에 추가한다.",
      "reason": "영어 결합어가 실제 동작 (확률 계산 및 임계값 필터링) 을 가린다."
    },
    {
      "id": "TUNE-12",
      "decision": "구체화 필요",
      "suggested_revision": "모든 권한을 세션에 통합하면 구현은 단순하지만 보안 위험이 있다.",
      "reason": "'한 바구니', '싸다' 비유가 구현 단순성과 보안 위험의 trade-off 를 가린다."
    },
    {
      "id": "TUNE-CTL-01",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체, 대상, 형식, 조건이 명확하다."
    },
    {
      "id": "TUNE-CTL-02",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "조건, 주체, 결과가 명시적이다."
    },
    {
      "id": "TUNE-CTL-03",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체, 시점, 조건, 동작이 명확하다."
    }
  ]
}
