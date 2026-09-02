{
  "cases": [
    {
      "id": "NAT-01",
      "decision": "구체화 필요",
      "suggested_revision": "두 화면 형태의 표시 필드를 같게 맞춘다.",
      "reason": "영어 용어 variant 와 parity 는 설계 문서 정의가 없으면 사용자에게 화면 형태와 필드 일치라는 의미가 전달되지 않는다."
    },
    {
      "id": "NAT-02",
      "decision": "구체화 필요",
      "suggested_revision": "응답 객체에 status 속성을 추가해 화면이 읽을 수 있게 한다.",
      "reason": "구멍을 연다는 비유가 실제 동작 (속성 추가 및 공개) 을 모호하게 만든다."
    },
    {
      "id": "NAT-03",
      "decision": "구체화 필요",
      "suggested_revision": "호출 경로에 포함되지만 변경하지 않는다.",
      "reason": "주체와 서술어가 생략된 명사 나열로, 문맥 없이는 호출 대상과 변경 여부를 확정하기 어렵다."
    },
    {
      "id": "NAT-04",
      "decision": "구체화 필요",
      "suggested_revision": "클라이언트만 먼저 배포해도 기존 로그인 기능은 정상 동작한다.",
      "reason": "무해하다는 평가가 구체적인 기능 동작 보장 (로그인, 로그아웃, 세션 갱신) 으로 대체되어야 한다."
    },
    {
      "id": "NAT-05",
      "decision": "구체화 필요",
      "suggested_revision": "로봇 경로 재계산 작업의 동시 처리 묶음 수를 제한한다.",
      "reason": "fleet, fan-out 등 영어 복합 명사가 실제 제어 대상 (동시 처리 묶음 수) 을 가린다."
    },
    {
      "id": "NAT-06",
      "decision": "구체화 필요",
      "suggested_revision": "이벤트를 Kafka 정산 토픽에 발행한다.",
      "reason": "파이프에 태운다는 비유가 실제 기술 동작 (Kafka 토픽 발행) 을 불명확하게 한다."
    },
    {
      "id": "NAT-07",
      "decision": "구체화 필요",
      "suggested_revision": "이 방식은 기존 분개 이력을 수정하지 않고 보존한다.",
      "reason": "회계 오염이라는 평가가 구체적인 사실 (기존 분개 보존) 로 대체되어야 한다."
    },
    {
      "id": "NAT-08",
      "decision": "구체화 필요",
      "suggested_revision": "기동 시 사전 적재를 활성화하는 것이 비용 대비 효과적이다.",
      "reason": "쌉니다라는 구어체와 모호한 비용 표현이 기술적 판단 근거 (메모리 대비 응답 시간 개선) 로 명확해야 한다."
    },
    {
      "id": "NAT-09",
      "decision": "구체화 필요",
      "suggested_revision": "`EnrollmentWizard` 가 네 단계의 이동과 입력값 보존을 담당합니다.",
      "reason": "오케스트레이션이라는 영어 동사를 한국어 역할 설명으로 바꾸고, 코드 이름을 한 번 병기해야 한다."
    },
    {
      "id": "CTL-01",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "표준 용어집에 정의된 영어 용어를 사용하며 대상, 조건, 동작이 명확하다."
    },
    {
      "id": "CTL-02",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "코드 식별자를 정확히 유지하며 주체와 동작이 명확하게 표현되었다."
    },
    {
      "id": "CTL-03",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "저장값, 검사 시점, 동작 조건이 문장 자체로 명확하게 설명되었다."
    }
  ]
}
