{
  "cases": [
    {
      "id": "NAT-01",
      "decision": "구체화 필요",
      "suggested_revision": "관리자용 화면과 학생용 화면의 표시 필드를 같게 맞춘다.",
      "reason": "영어 일반어와 한국어가 결합된 명사 나열로 대상과 동작이 가려졌다."
    },
    {
      "id": "NAT-02",
      "decision": "구체화 필요",
      "suggested_revision": "API 응답 객체에 `status` 속성을 추가해 화면이 상태를 읽을 수 있게 한다.",
      "reason": "비유가 실제 동작(속성 추가 및 공개)을 대신하고 있다."
    },
    {
      "id": "NAT-03",
      "decision": "구체화 필요",
      "suggested_revision": "`LegacyAuthAdapter`는 호출 경로에 포함되지만 이번 작업에서는 변경하지 않는다.",
      "reason": "주체와 서술어가 빠진 과도한 압축으로 독자가 조사와 동작을 채워야 한다."
    },
    {
      "id": "NAT-04",
      "decision": "구체화 필요",
      "suggested_revision": "클라이언트만 먼저 배포해도 기존 로그인, 로그아웃, 세션 갱신 동작은 바뀌지 않는다.",
      "reason": "평가(무해하다)가 조건과 결과(기존 동작 유지)를 대신하고 있다."
    },
    {
      "id": "NAT-05",
      "decision": "구체화 필요",
      "suggested_revision": "500대 로봇 전체의 경로 재계산 작업을 25대씩 묶음으로 나누고, 동시에 처리하는 묶음을 최대 네 개로 제한한다.",
      "reason": "영어 일반어와 음역어가 결합된 명사 나열로 실제 동작(묶음 분할 및 동시 처리 제한)이 가려졌다."
    },
    {
      "id": "NAT-06",
      "decision": "구체화 필요",
      "suggested_revision": "`payment_completed` 이벤트를 Kafka의 `settlement-events` 토픽에 발행한다.",
      "reason": "비유(파이프에 태운다)가 실제 동작(토픽 발행)을 대신하고 있다."
    },
    {
      "id": "NAT-07",
      "decision": "구체화 필요",
      "suggested_revision": "이 방식은 기존 분개 이력과 수정 근거를 모두 남긴다.",
      "reason": "평가와 비유(회계 오염을 막는다)가 실제 효과(이력 및 근거 보존)를 대신하고 있다."
    },
    {
      "id": "NAT-08",
      "decision": "구체화 필요",
      "suggested_revision": "응답 시간 개선이 추가 메모리 비용보다 중요하므로 모든 운영 서버에서 기동 시 사전 적재를 활성화한다.",
      "reason": "구어체와 평가(싸다)가 결정의 근거와 조건을 대신하고 있다."
    },
    {
      "id": "NAT-09",
      "decision": "구체화 필요",
      "suggested_revision": "`EnrollmentWizard`는 네 단계의 이동과 입력값 보존을 담당한다.",
      "reason": "음역어와 영어 일반어(오케스트레이션)가 결합해 실제 동작(단계 이동 및 입력값 보존)을 가리고 있다."
    },
    {
      "id": "CTL-01",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "대상, 조건, 동작이 모두 분명하며 용어집에 정의된 표준 용어를 사용했다."
    },
    {
      "id": "CTL-02",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체, 값, 대상 속성이 명시돼 있으며 코드 식별자를 올바르게 보존했다."
    },
    {
      "id": "CTL-03",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "저장값, 검사 시점, 동작이 문장 자체로 분명하게 설명되어 있다."
    }
  ]
}
