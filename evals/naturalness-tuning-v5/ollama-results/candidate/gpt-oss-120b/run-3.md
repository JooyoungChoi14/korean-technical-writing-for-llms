{
  "cases": [
    {
      "id": "TUNE-01",
      "decision": "구체화 필요",
      "suggested_revision": "권한 서비스는 각 기관의 권한 설정 스냅샷을 병합한다.",
      "reason": "‘tenant’, ‘entitlement snapshot’, ‘머지한다’는 영어·은어 혼용이며 주체가 명시되지 않아 독자가 동작 주체와 대상(기관·스냅샷)을 추론해야 함."
    },
    {
      "id": "TUNE-02",
      "decision": "구체화 필요",
      "suggested_revision": "주문 서비스는 실패한 주문에 대해 `inventory-retry` 토픽에 이벤트를 발행한다.",
      "reason": "‘레일’이라는 은유적 표현과 주체 누락으로 어떤 작업이 수행되는지 불명확함."
    },
    {
      "id": "TUNE-03",
      "decision": "구체화 필요",
      "suggested_revision": "먼저 모든 행을 검증하고, 검증이 통과하면 데이터를 저장한다.",
      "reason": "명사 나열만으로 주체·동작·조건·결과가 모두 생략돼 독자가 의미를 재구성해야 함."
    },
    {
      "id": "TUNE-04",
      "decision": "구체화 필요",
      "suggested_revision": "응답이 없거나 ‘응답하지 않음’인 경우를 제외하는 로직은 통계 왜곡을 방지한다.",
      "reason": "'분기'라는 은유와 동작·조건이 명시되지 않아 어떤 상황을 말하는지 모호함."
    },
    {
      "id": "TUNE-05",
      "decision": "의미 확인 필요",
      "suggested_revision": "SettlementReconciliationJob은 차이 내역을 확인하지만 차이를 자동으로 해결하지 않는다.",
      "reason": "원문에서는 배치가 차이를 자동으로 수정·승인하지 않는다고 명시했으나, 제시 문장은 ‘차이를 클로즈한다’라고 반대 의미를 전달함. 의미가 일치하도록 수정 필요."
    },
    {
      "id": "TUNE-06",
      "decision": "구체화 필요",
      "suggested_revision": "캐시를 사전에 로드해 두는 것이 이득이다.",
      "reason": "'데워두는'이라는 은유가 기술적 동작을 명확히 전달하지 않으며, 보다 직접적인 표현이 필요함."
    },
    {
      "id": "TUNE-07",
      "decision": "구체화 필요",
      "suggested_revision": "권한 서비스는 approval matrix의 effective rule을 구체화한다.",
      "reason": "‘materialize’와 같은 영어 은어가 사용돼 의미가 불분명하고, 주체가 명시되지 않음."
    },
    {
      "id": "TUNE-08",
      "decision": "구체화 필요",
      "suggested_revision": "권한 서비스는 권한 변경 이벤트를 감사 스트림에 전송한다.",
      "reason": "'흘린다'라는 은유적 표현이 구체적인 동작(이벤트 발행)을 전달하지 못함."
    },
    {
      "id": "TUNE-09",
      "decision": "구체화 필요",
      "suggested_revision": "기존 API는 유지하고, 신규 필드는 선택적으로 적용한다.",
      "reason": "명사 나열만으로 동작·조건이 빠져 있어 독자가 의미를 추론해야 함."
    },
    {
      "id": "TUNE-10",
      "decision": "의미 확인 필요",
      "suggested_revision": "소급 수정은 원장을 직접 수정하지 않고, 반대 분개와 새로운 환불 분개를 추가한다.",
      "reason": "원문은 원장을 직접 수정·삭제하지 않으며, 반대 분개와 새 분개를 추가한다고 설명하지만 제시 문장은 ‘오염시킨다’라는 반대 의미를 담고 있어 의미 불일치."
    },
    {
      "id": "TUNE-11",
      "decision": "구체화 필요",
      "suggested_revision": "예측 모델이 세그먼트에 점수를 매기고, 컷오프를 적용한다.",
      "reason": "'스코어링', '어플라이' 등 영어 은어가 사용돼 한국어 독자에게 동작이 명확히 전달되지 않음."
    },
    {
      "id": "TUNE-12",
      "decision": "구체화 필요",
      "suggested_revision": "모든 권한을 하나의 세션 값에 합치면 구현이 단순해지지만, 조직 이동 후 로그아웃 전까지 이전 권한이 남는다.",
      "reason": "'한 바구니에 담으면 싸다'라는 은유와 평가가 실제 동작·부작용을 충분히 설명하지 못함."
    },
    {
      "id": "TUNE-CTL-01",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "식별자 형식, 저장소, 만료 시간 모두 명확히 기술돼 있어 추가 수정이 필요하지 않음."
    },
    {
      "id": "TUNE-CTL-02",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "조건·동작이 모두 구체적으로 서술돼 있어 자연스럽고 명확함."
    },
    {
      "id": "TUNE-CTL-03",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체, 시점, 비교값, 조건·동작이 완전하게 기술돼 있음."
    }
  ]
}
