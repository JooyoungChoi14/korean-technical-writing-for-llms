{
  "cases": [
    {
      "id": "TUNE-01",
      "decision": "구체화 필요",
      "suggested_revision": "세 기관의 권한 설정과 공통 역할 설정에서 허용된 메뉴를 합친다.",
      "reason": "merge, snapshot, tenant를 음역어와 결합해 독자가 실제 동작(설정 읽기 → 메뉴 합치기)을 복원해야 함"
    },
    {
      "id": "TUNE-02",
      "decision": "구체화 필요",
      "suggested_revision": "`inventory_retry_requested` 이벤트를 `inventory-retry` 토픽에 발행한다.",
      "reason": "재처리 레일이라는 비유가 실제 동작(Kafka 토픽 발행)을 가림"
    },
    {
      "id": "TUNE-03",
      "decision": "구체화 필요",
      "suggested_revision": "모든 행을 검사한 뒤 유효할 때만 저장한다.",
      "reason": "검증 선행·반영 후속이라는 명사 나열이 주체·서술어 없이 압축되어 문맥 없이 읽기 어려움"
    },
    {
      "id": "TUNE-04",
      "decision": "구체화 필요",
      "suggested_revision": "이 조건문은 응답하지 않은 문항과 이탈로 값이 없는 문항을 평균 계산에서 제외한다.",
      "reason": "통계 왜곡 방지라는 평가가 실제 동작(특정 값 제외)을 대신함"
    },
    {
      "id": "TUNE-05",
      "decision": "구체화 필요",
      "suggested_revision": "정산 조정 배치(`SettlementReconciliationJob`)가 차이 내역을 예외 목록에 추가한다.",
      "reason": "리컨실리에이션, 잡, 클로즈라는 음역어 결합이 독자가 알 수 없는 동작(예외 목록 추가)을 가림"
    },
    {
      "id": "TUNE-06",
      "decision": "구체화 필요",
      "suggested_revision": "서버 기동 시 자주 조회하는 상품을 로컬 캐시에 미리 적재하면 배포 직후 검색 응답 지연이 줄어든다.",
      "reason": "이득이라는 평가가 실제 효과(지연 감소)와 조건(사전 적재)을 대신함"
    },
    {
      "id": "TUNE-07",
      "decision": "구체화 필요",
      "suggested_revision": "직급·부서·사용자별 승인 규칙을 계산해 최종 승인 한도를 저장한다.",
      "reason": "approval matrix, effective rule, materialize를 음역어로만 결합해 독자가 동작을 복원해야 함"
    },
    {
      "id": "TUNE-08",
      "decision": "구체화 필요",
      "suggested_revision": "`access_role_changed` 이벤트를 `access-audit` 토픽에 발행한다.",
      "reason": "감사 스트림에 흘린다는 비유가 실제 동작(Kafka 토픽 발행)을 가림"
    },
    {
      "id": "TUNE-09",
      "decision": "구체화 필요",
      "suggested_revision": "기존 엔드포인트와 필드를 유지하고 `preferredName` 필드를 신버전 앱만 읽도록 추가한다.",
      "reason": "신규 필드 선택 적용이라는 명사 압축이 누가 무엇을 읽는지 가림"
    },
    {
      "id": "TUNE-10",
      "decision": "구체화 필요",
      "suggested_revision": "마감된 원장은 수정하지 않고 정정 분개를 현재 기간에 새로 기록한다.",
      "reason": "소급 수정과 오염이라는 평가가 실제 동작(현재 기간 기록)을 대신함"
    },
    {
      "id": "TUNE-11",
      "decision": "구체화 필요",
      "suggested_revision": "모델이 고객별 이탈 확률을 계산하고 0.7 이상인 고객을 검토 목록에 추가한다.",
      "reason": "세그먼트, 스코어링, 컷오프, 어플라이를 음역어로만 결합해 독자가 동작을 복원해야 함"
    },
    {
      "id": "TUNE-12",
      "decision": "구체화 필요",
      "suggested_revision": "두 권한을 하나의 세션 값으로 합치면 구현은 단순하지만 조직 이동 뒤 로그아웃할 때까지 이전 행을 볼 수 있다.",
      "reason": "한 바구니에 담으면 싸다는 비유가 실제 결과(조직 이동 뒤 권한 불일치)를 가림"
    },
    {
      "id": "TUNE-CTL-01",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체(무엇을), 동작(만들고 저장), 형식, 저장소, 조건(10분)이 모두 명시됨"
    },
    {
      "id": "TUNE-CTL-02",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "프로젝트 용어집에 정의된 Kubernetes 용어를 사용하며 주체, 조건, 동작이 명확함"
    },
    {
      "id": "TUNE-CTL-03",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체(권한 서비스), 시점(요청마다), 비교값, 조건, 동작(거부)이 모두 명시됨"
    }
  ]
}
