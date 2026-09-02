{
  "cases": [
    {
      "id": "TUNE-01",
      "decision": "구체화 필요",
      "suggested_revision": "권한 서비스는 각 tenant의 entitlement snapshot을 병합한다.",
      "reason": "‘머지한다’는 영어식 표현이며, 주체가 명시되지 않아 독자가 동작 주체를 추론해야 함."
    },
    {
      "id": "TUNE-02",
      "decision": "구체화 필요",
      "suggested_revision": "실패한 주문을 재처리 큐에 넣는다.",
      "reason": "‘레일’이라는 은유가 구체적인 큐를 가리키는지 불명확하고, 동작 대상이 명시되지 않음."
    },
    {
      "id": "TUNE-03",
      "decision": "구체화 필요",
      "suggested_revision": "검증을 먼저 수행하고, 그 후에 반영한다.",
      "reason": "명사 나열만으로는 주체·동작·순서를 파악하기 어려워 독자가 재구성해야 함."
    },
    {
      "id": "TUNE-04",
      "decision": "구체화 필요",
      "suggested_revision": "이 조건문은 통계 왜곡을 방지한다.",
      "reason": "‘분기’가 ‘조건문’인지 ‘분기(quarter)’인지 모호하고, 평가가 앞에 나와 의미가 흐려짐."
    },
    {
      "id": "TUNE-05",
      "decision": "구체화 필요",
      "suggested_revision": "정산 조정 작업이 차이를 해결한다.",
      "reason": "‘리컨실리에이션’, ‘잡’, ‘클로즈한다’ 등 영어식 용어와 은유가 혼합돼 실제 동작을 파악하기 어려움."
    },
    {
      "id": "TUNE-06",
      "decision": "구체화 필요",
      "suggested_revision": "캐시를 처음부터 미리 로드해 두는 것이 이득이다.",
      "reason": "‘데워두는’이라는 은유가 구체적인 사전 적재 동작을 명시하지 않아 독자가 의미를 추론해야 함."
    },
    {
      "id": "TUNE-07",
      "decision": "구체화 필요",
      "suggested_revision": "approval matrix의 effective rule을 구체화한다.",
      "reason": "‘materialize’와 같은 영어식 동사가 의미를 모호하게 만들고, 한국어 표현이 필요함."
    },
    {
      "id": "TUNE-08",
      "decision": "구체화 필요",
      "suggested_revision": "권한 변경 이벤트를 감사 스트림에 전송한다.",
      "reason": "‘흘린다’는 은유적 표현으로 실제 발행 동작을 명확히 전달하지 못함."
    },
    {
      "id": "TUNE-09",
      "decision": "구체화 필요",
      "suggested_revision": "기존 API를 유지하고, 신규 필드는 선택적으로 적용한다.",
      "reason": "명사 나열만으로는 동작 순서와 조건이 불분명함."
    },
    {
      "id": "TUNE-10",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "‘소급 수정은 원장을 오염시킨다’는 대상·동작·결과가 명확히 제시돼 독자가 추가 해석이 필요 없음."
    },
    {
      "id": "TUNE-11",
      "decision": "구체화 필요",
      "suggested_revision": "예측 모델이 세그먼트에 점수를 매기고 임계값을 적용한다.",
      "reason": "‘스코어링’, ‘컷오프’, ‘어플라이한다’ 등 영어식 용어가 혼용돼 의미 파악에 부담을 줌."
    },
    {
      "id": "TUNE-12",
      "decision": "구체화 필요",
      "suggested_revision": "모든 권한을 하나의 세션 값에 합치면 구현이 단순해진다.",
      "reason": "‘한 바구니에 담으면 싸다’는 은유가 실제 기술적 효과를 명확히 전달하지 못함."
    },
    {
      "id": "TUNE-CTL-01",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "문장이 명확히 식별자 형식, 저장소, 만료 시간을 전달하고 있어 재구성이 필요 없음."
    },
    {
      "id": "TUNE-CTL-02",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "조건·동작이 모두 명시돼 이해에 어려움이 없음."
    },
    {
      "id": "TUNE-CTL-03",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체·시점·비교값·조건·동작이 모두 구체적으로 서술돼 명확함."
    }
  ]
}
