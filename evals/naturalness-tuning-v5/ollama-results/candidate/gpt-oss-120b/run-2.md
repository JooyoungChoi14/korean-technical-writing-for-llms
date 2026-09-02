{
  "cases": [
    {
      "id": "TUNE-01",
      "decision": "구체화 필요",
      "suggested_revision": "각 기관의 권한 스냅샷을 병합한다.",
      "reason": "‘tenant’·‘entitlement snapshot’·‘머지한다’ 등 영문 혼용과 은유적 표현이 있어 독자가 대상·동작을 바로 파악하기 어렵다."
    },
    {
      "id": "TUNE-02",
      "decision": "구체화 필요",
      "suggested_revision": "실패한 주문을 `inventory-retry` 토픽에 발행한다.",
      "reason": "‘재처리 레일’이라는 은유가 실제 동작(이벤트 발행)을 명확히 전달하지 않는다."
    },
    {
      "id": "TUNE-03",
      "decision": "구체화 필요",
      "suggested_revision": "먼저 모든 행을 검증하고, 검증이 통과하면 데이터를 저장한다.",
      "reason": "‘검증 선행, 반영 후속’은 주어·동사가 없고 의미가 압축돼 독자가 흐름을 추론해야 함."
    },
    {
      "id": "TUNE-04",
      "decision": "구체화 필요",
      "suggested_revision": "이 조건문은 통계 왜곡을 방지한다.",
      "reason": "‘이 분기’라는 표현이 무엇을 가리키는지 불명확하고, 동작을 명시하지 않는다."
    },
    {
      "id": "TUNE-05",
      "decision": "의미 확인 필요",
      "suggested_revision": "정산 리컨실리에이션 잡은 차이를 확인하고 예외 목록에 추가한다.",
      "reason": "원문에서는 배치가 차이를 자동으로 수정·승인하지 않는다고 명시했으나, 제시된 문장은 차이를 ‘클로즈한다’고 잘못 서술하고 있다."
    },
    {
      "id": "TUNE-06",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "‘캐시는 처음부터 데워두는 편이 이득이다’는 의미가 명확하고, 문맥과 일치한다."
    },
    {
      "id": "TUNE-07",
      "decision": "구체화 필요",
      "suggested_revision": "approval matrix의 effective rule을 구체화한다.",
      "reason": "‘materialize한다’ 등 영문 혼용이 있어 한국어 독자가 동작을 바로 이해하기 어렵다."
    },
    {
      "id": "TUNE-08",
      "decision": "구체화 필요",
      "suggested_revision": "권한 변경 이벤트를 감사 스트림에 전송한다.",
      "reason": "‘흘린다’라는 은유가 실제 발행 동작을 명확히 전달하지 않는다."
    },
    {
      "id": "TUNE-09",
      "decision": "구체화 필요",
      "suggested_revision": "기존 API는 유지하고, 신규 필드는 선택적으로 적용한다.",
      "reason": "‘기존 API 유지, 신규 필드 선택 적용’은 동사와 연결어가 부족해 의미가 불분명하다."
    },
    {
      "id": "TUNE-10",
      "decision": "의미 확인 필요",
      "suggested_revision": "소급 수정은 원장을 오염시키지 않는다.",
      "reason": "문맥에서는 소급 입력이 원장을 변경하지 않고 새 분개를 추가한다고 설명했으나, 제시 문장은 반대 의미를 담고 있다."
    },
    {
      "id": "TUNE-11",
      "decision": "구체화 필요",
      "suggested_revision": "예측 모델이 세그먼트를 점수화하고 임계값을 적용한다.",
      "reason": "‘스코어링’, ‘컷오프’, ‘어플라이한다’ 등 영문 용어가 혼용돼 독자가 정확한 동작을 파악하기 어렵다."
    },
    {
      "id": "TUNE-12",
      "decision": "구체화 필요",
      "suggested_revision": "모든 권한을 하나의 세션 값에 합치면 구현이 단순해진다.",
      "reason": "‘한 바구니에 담으면 싸다’는 은유가 구체적인 동작·효과를 전달하지 않는다."
    },
    {
      "id": "TUNE-CTL-01",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "문장이 명확하고, 필요한 식별자·저장소·만료 시간을 정확히 전달한다."
    },
    {
      "id": "TUNE-CTL-02",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "조건·결과가 모두 명시된 자연스러운 한국어 기술 문장이다."
    },
    {
      "id": "TUNE-CTL-03",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체·검사 시점·비교값·조건·동작이 모두 명확히 서술되어 있다."
    }
  ]
}
