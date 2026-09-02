{
  "cases": [
    {
      "id": "TUNE-01",
      "decision": "구체화 필요",
      "suggested_revision": "각 기관(tenant)의 권한 설정 스냅샷을 병합한다.",
      "reason": "영어 용어와 ‘머지’라는 혼합어가 포함돼 독자가 실제 동작(병합)을 바로 이해하기 어렵다."
    },
    {
      "id": "TUNE-02",
      "decision": "구체화 필요",
      "suggested_revision": "실패한 주문을 재처리 토픽(inventory-retry)으로 발행한다.",
      "reason": "‘레일’이라는 은유가 실제 작업(이벤트 발행)을 명확히 전달하지 않는다."
    },
    {
      "id": "TUNE-03",
      "decision": "구체화 필요",
      "suggested_revision": "먼저 검증을 수행하고, 검증이 통과하면 데이터를 반영한다.",
      "reason": "‘검증 선행, 반영 후속’은 주어·동사가 생략된 압축된 명사열이라 독자가 절차를 추론해야 함."
    },
    {
      "id": "TUNE-04",
      "decision": "구체화 필요",
      "suggested_revision": "이 조건문은 통계 왜곡을 방지한다.",
      "reason": "‘분기’라는 추상적 표현이 실제 역할(통계 왜곡 방지)을 충분히 전달하지 않는다."
    },
    {
      "id": "TUNE-05",
      "decision": "구체화 필요",
      "suggested_revision": "정산 리컨실리에이션 작업이 차이를 정리한다.",
      "reason": "‘리컨실리에이션’, ‘잡’, ‘클로즈’ 등 혼합된 영·한 용어와 은유가 의미를 모호하게 만든다."
    },
    {
      "id": "TUNE-06",
      "decision": "구체화 필요",
      "suggested_revision": "캐시를 미리 로드해 두는 것이 이득이다.",
      "reason": "‘데워두는’이라는 은유가 실제 동작(프리로드)을 명확히 설명하지 않는다."
    },
    {
      "id": "TUNE-07",
      "decision": "구체화 필요",
      "suggested_revision": "approval matrix의 effective rule을 실제 규칙으로 구현한다.",
      "reason": "‘materialize’와 같은 영문 동사가 의미를 추정하게 만들며, 한국어 독자에게 불명확하다."
    },
    {
      "id": "TUNE-08",
      "decision": "구체화 필요",
      "suggested_revision": "권한 변경 이벤트를 감사 스트림에 전송한다.",
      "reason": "‘흘린다’라는 은유가 이벤트 발행이라는 구체적 동작을 전달하지 않는다."
    },
    {
      "id": "TUNE-09",
      "decision": "구체화 필요",
      "suggested_revision": "기존 API는 유지하고, 신규 필드는 선택적으로 적용한다.",
      "reason": "‘기존 API 유지, 신규 필드 선택 적용’은 동사와 연결어가 부족해 의미를 바로 파악하기 어렵다."
    },
    {
      "id": "TUNE-10",
      "decision": "의미 확인 필요",
      "suggested_revision": "소급 수정은 원장을 직접 수정하지 않는다.",
      "reason": "문장이 원본 설명(원장을 수정·삭제하지 않음)과 반대되는 평가를 담고 있어 의미가 모순된다."
    },
    {
      "id": "TUNE-11",
      "decision": "구체화 필요",
      "suggested_revision": "예측 모델이 세그먼트를 점수화하고 임계값을 적용한다.",
      "reason": "‘스코어링’, ‘컷오프’를 그대로 사용하면 한국어 독자가 실제 동작을 추론해야 한다."
    },
    {
      "id": "TUNE-12",
      "decision": "구체화 필요",
      "suggested_revision": "모든 권한을 하나의 세션 값에 합치면 구현이 단순해진다.",
      "reason": "'싸다'라는 은유가 실제 효과(구현 단순화)를 명확히 전달하지 않는다."
    },
    {
      "id": "TUNE-CTL-01",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "문장이 명확하고, 식별자·키 형식·저장 기간을 정확히 전달한다."
    },
    {
      "id": "TUNE-CTL-02",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "조건·결과가 모두 포함된 자연스러운 한국어 문장이다."
    },
    {
      "id": "TUNE-CTL-03",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체·시점·비교·조건·동작이 모두 명시돼 의미가 완전하게 전달된다."
    }
  ]
}
