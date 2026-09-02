{
  "cases": [
    {
      "id": "TUNE-01",
      "decision": "구체화 필요",
      "suggested_revision": "각 기관의 권한 설정을 병합한다.",
      "reason": "‘tenant’, ‘entitlement snapshot’, ‘머지’ 등 영어 혼용과 추상적 표현으로 대상과 동작이 명확하지 않음."
    },
    {
      "id": "TUNE-02",
      "decision": "구체화 필요",
      "suggested_revision": "실패한 주문을 `inventory-retry` 토픽에 발행한다.",
      "reason": "‘레일’이라는 용어가 모호하고, 실제 동작(이벤트 발행)을 명확히 서술하지 않음."
    },
    {
      "id": "TUNE-03",
      "decision": "구체화 필요",
      "suggested_revision": "검증을 먼저 수행하고, 검증이 통과하면 데이터를 저장한다.",
      "reason": "‘검증 선행, 반영 후속’은 주어·동사가 없고 의미가 압축돼 독자가 추론해야 함."
    },
    {
      "id": "TUNE-04",
      "decision": "구체화 필요",
      "suggested_revision": "이 조건문은 통계 왜곡을 방지한다.",
      "reason": "‘분기’가 비유적이며, 실제 동작(조건문)이 무엇인지 명시되지 않음."
    },
    {
      "id": "TUNE-05",
      "decision": "구체화 필요",
      "suggested_revision": "정산 리컨실리에이션 작업은 차이 내역을 예외 목록에 추가한다.",
      "reason": "‘리컨실리에이션’, ‘잡’, ‘클로즈’ 등 영어 혼용과 의미가 원문과 맞지 않아 정확한 동작을 제시해야 함."
    },
    {
      "id": "TUNE-06",
      "decision": "구체화 필요",
      "suggested_revision": "캐시는 사전 적재하는 것이 이득이다.",
      "reason": "‘데워두는’이라는 비유적 표현이 기술 문서에 부적절하고, 동작을 명확히 서술해야 함."
    },
    {
      "id": "TUNE-07",
      "decision": "구체화 필요",
      "suggested_revision": "approval matrix의 effective rule을 실제 값으로 저장한다.",
      "reason": "‘materialize’ 등 영어 동사가 의미를 가리키지 않아 한국어로 구체적인 동작을 제시해야 함."
    },
    {
      "id": "TUNE-08",
      "decision": "구체화 필요",
      "suggested_revision": "권한 변경을 감사 스트림에 전송한다.",
      "reason": "‘흘린다’는 비유적 표현으로 동작을 명확히 전달하지 못함."
    },
    {
      "id": "TUNE-09",
      "decision": "구체화 필요",
      "suggested_revision": "기존 API는 유지하고, 신규 필드는 선택적으로 적용한다.",
      "reason": "‘기존 API 유지, 신규 필드 선택 적용’은 동사와 연결어가 부족해 의미가 불분명함."
    },
    {
      "id": "TUNE-10",
      "decision": "의미 확인 필요",
      "suggested_revision": null,
      "reason": "‘소급 수정은 원장을 오염시킨다’는 문장이 문맥(원장을 직접 수정하지 않고 반대 분개를 추가)과 상충함. 정확한 의미를 확인해야 함."
    },
    {
      "id": "TUNE-11",
      "decision": "구체화 필요",
      "suggested_revision": "예측 모델이 세그먼트에 점수를 매기고 임계값을 적용한다.",
      "reason": "‘스코어링’, ‘컷오프’, ‘어플라이’ 등 영어 용어가 혼용돼 동작을 명확히 전달하지 못함."
    },
    {
      "id": "TUNE-12",
      "decision": "구체화 필요",
      "suggested_revision": "모든 권한을 하나의 세션 값에 합치면 구현이 단순해지지만, 보안 위험이 있다.",
      "reason": "‘한 바구니에 담으면 싸다’는 비유적·평가적 표현으로 실제 동작과 부작용을 구체적으로 서술해야 함."
    },
    {
      "id": "TUNE-CTL-01",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "문장이 명확하고, 식별자·키 형식·저장 기간을 정확히 전달하고 있음."
    },
    {
      "id": "TUNE-CTL-02",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "조건·대상·결과가 모두 명확히 서술된 자연스러운 기술 문장임."
    },
    {
      "id": "TUNE-CTL-03",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체·시점·비교값·조건·동작이 모두 완전하게 기술되어 있음."
    }
  ]
}
