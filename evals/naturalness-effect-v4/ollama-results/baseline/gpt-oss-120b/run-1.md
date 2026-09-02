{
  "cases": [
    {
      "id": "NAT-01",
      "decision": "구체화 필요",
      "suggested_revision": "두 화면 형태가 표시하는 필드가 동일하도록 한다.",
      "reason": "영어 용어와 명사 문자열만으로는 ‘variant’와 ‘parity’가 무엇을 의미하는지 독자가 추론해야 함."
    },
    {
      "id": "NAT-02",
      "decision": "구체화 필요",
      "suggested_revision": "화면이 상태 값을 읽을 수 있도록 API 응답에 `status` 속성을 추가한다.",
      "reason": "‘상태를 화면으로 꺼낼 구멍을 연다’는 비유적 표현으로 실제 동작(속성 공개)을 명확히 전달하지 못함."
    },
    {
      "id": "NAT-03",
      "decision": "구체화 필요",
      "suggested_revision": "이 모듈은 호출 경로에 포함되지만, 변경은 필요하지 않다.",
      "reason": "‘호출 경유, 변경 불요’는 주어·동사가 생략된 압축된 명사 나열이라 독자가 의미를 재구성해야 함."
    },
    {
      "id": "NAT-04",
      "decision": "구체화 필요",
      "suggested_revision": "클라이언트만 먼저 배포해도 기존 기능에 영향을 주지 않는다.",
      "reason": "‘무해하다’라는 평가가 사실을 대신하고, 구체적인 영향 범위가 명시되지 않음."
    },
    {
      "id": "NAT-05",
      "decision": "구체화 필요",
      "suggested_revision": "500대 로봇에 대해 경로 재계산을 여러 묶음으로 나누어 수행하도록 제어한다.",
      "reason": "영어 혼용·명사 문자열로 인해 대상(로봇)·동작(재계산을 나누어 수행)·범위가 불명확함."
    },
    {
      "id": "NAT-06",
      "decision": "구체화 필요",
      "suggested_revision": "이벤트를 Kafka `settlement-events` 토픽에 발행한다.",
      "reason": "‘정산 파이프에 태운다’는 은유적 표현으로 실제 작업(토픽에 발행)을 명확히 전달하지 않음."
    },
    {
      "id": "NAT-07",
      "decision": "구체화 필요",
      "suggested_revision": "이 방식은 기존 분개 이력과 수정 근거를 모두 보존한다.",
      "reason": "‘회계 오염을 막는다’는 평가형 표현으로, 실제 목적(이력·근거 보존)을 구체적으로 제시하지 않음."
    },
    {
      "id": "NAT-08",
      "decision": "구체화 필요",
      "suggested_revision": "시작 시에 사전 적재를 활성화하면 응답 시간이 크게 감소한다.",
      "reason": "‘처음부터 켜두는 편이 쌉니다’는 구어·비유적 표현으로, 결정 이유와 효과를 명확히 전달하지 못함."
    },
    {
      "id": "NAT-09",
      "decision": "구체화 필요",
      "suggested_revision": "수강신청 위저드 화면이 네 단계를 순차적으로 진행한다.",
      "reason": "‘위저드’, ‘오케스트레이션’ 등 영어 혼용과 은유가 독자가 실제 동작을 추론하도록 함."
    },
    {
      "id": "CTL-01",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "대상·조건·동작이 모두 명시된 명료한 문장."
    },
    {
      "id": "CTL-02",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체·값·대상이 명확히 제시된 간결한 기술 문장."
    },
    {
      "id": "CTL-03",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체·조건·동작이 모두 포함된 명확한 설명."
    }
  ]
}
