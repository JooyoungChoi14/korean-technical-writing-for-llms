{
  "cases": [
    {
      "id": "TUNE-01",
      "decision": "구체화 필요",
      "suggested_revision": "세 기관의 권한 설정과 공통 역할 설정에서 허용 메뉴를 읽어 합친다.",
      "reason": "tenant와 entitlement snapshot을 음역어 그대로 쓰고, 머지(merge)라는 동사가 어떤 속성을 어떻게 합치는지 가린다. 문맥의 '허용 메뉴를 합친다'를 직접 드러내야 한다."
    },
    {
      "id": "TUNE-02",
      "decision": "구체화 필요",
      "suggested_revision": "주문 서비스가 `inventory_retry_requested` 이벤트를 `inventory-retry` 토픽에 발행한다.",
      "reason": "'재처리 레일에 올린다'는 비유가 실제 동작(이벤트 발행)과 대상(Kafka 토픽)을 가린다. 문맥에 있는 발행 동작과 토픽 이름을 명시해야 한다."
    },
    {
      "id": "TUNE-03",
      "decision": "구체화 필요",
      "suggested_revision": "모든 행을 검사한 뒤 유효할 때만 저장한다.",
      "reason": "명사만 나열해 주체와 서술어가 생략되었다. '검증 선행, 반영 후속'은 독자가 조사와 동작을 채워야 한다."
    },
    {
      "id": "TUNE-04",
      "decision": "구체화 필요",
      "suggested_revision": "값이 없는 문항을 평균 계산에서 제외한다.",
      "reason": "'통계 왜곡을 막는다'는 평가가 실제 동작(값 존재 확인 후 제외)을 대신한다. 문맥의 구체적인 조건과 동작을 드러내야 한다."
    },
    {
      "id": "TUNE-05",
      "decision": "구체화 필요",
      "suggested_revision": "정산 대조 배치(`SettlementReconciliationJob`)가 차이 내역을 예외 목록에 추가한다.",
      "reason": "'리컨실리에이션'을 '대조'로, '클로즈'를 '예외 목록 추가'로 구체화해야 한다. 문맥에서 배치가 자동 수정하거나 승인하지 않고 목록에만 추가한다고 명시되어 있다."
    },
    {
      "id": "TUNE-06",
      "decision": "구체화 필요",
      "suggested_revision": "서버 기동 시 상품 5만 건을 로컬 캐시에 미리 적재하면 배포 직후 검색 응답 p95가 420밀리초에서 90밀리초로 줄어든다.",
      "reason": "'데워둔다', '이득'은 비유와 평가이며 실제 동작(사전 적재)과 결과(지연 감소)를 가린다. 문맥의 구체적인 수치와 효과를 명시해야 한다."
    },
    {
      "id": "TUNE-07",
      "decision": "구체화 필요",
      "suggested_revision": "권한 서비스가 세 규칙을 미리 계산해 사용자별 최종 승인 한도를 저장한다.",
      "reason": "'approval matrix', 'effective rule', 'materialize'를 음역어와 기술 용어 그대로 쓰고 실제 동작(미리 계산해 저장)을 가린다."
    },
    {
      "id": "TUNE-08",
      "decision": "구체화 필요",
      "suggested_revision": "권한 서비스가 `access_role_changed` 이벤트를 `access-audit` 토픽에 발행한다.",
      "reason": "'감사 스트림에 흘린다'는 비유가 실제 동작(이벤트 발행)과 대상(Kafka 토픽)을 가린다."
    },
    {
      "id": "TUNE-09",
      "decision": "구체화 필요",
      "suggested_revision": "`/v1/profile` 엔드포인트와 기존 두 필드를 유지하고, 신버전 앱만 사용하는 선택 필드 `preferredName`을 추가한다.",
      "reason": "명사만 나열해 주체와 서술어가 생략되었다. 어떤 API를 유지하고 어떤 필드를 추가하는지 드러나지 않는다."
    },
    {
      "id": "TUNE-10",
      "decision": "구체화 필요",
      "suggested_revision": "마감 완료 원장은 수정하지 않고, 정정이 필요하면 현재 회계 기간에 반대 분개와 올바른 분개를 새로 기록한다.",
      "reason": "'소급 수정은 원장을 오염시킨다'는 평가가 실제 정책(마감 후 수정 금지와 현재 기간 정정 방식)을 대신한다."
    },
    {
      "id": "TUNE-11",
      "decision": "구체화 필요",
      "suggested_revision": "이탈 예측 모델이 고객별 확률을 계산하고, 분석 서비스가 0.7 이상인 고객을 상담 검토 목록에 추가한다.",
      "reason": "'세그먼트를 스코어링', '컷오프를 어플라이'는 음역어로 실제 동작(확률 계산, 임계값 적용)을 가린다. 주체도 모델과 서비스로 나뉘는데 문장에서 드러나지 않는다."
    },
    {
      "id": "TUNE-12",
      "decision": "구체화 필요",
      "suggested_revision": "메뉴 권한과 행 조회 권한을 하나의 세션 값으로 합치면 조직 이동 뒤 로그아웃할 때까지 이전 행을 볼 수 있다.",
      "reason": "'한 바구니에 담으면 싸다'는 비유가 실제 문제(조직 이동 후 권한 불일치)를 가린다. 문맥의 구체적인 부작용을 드러내야 한다."
    },
    {
      "id": "TUNE-CTL-01",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "대상(캐시 키), 형식, 저장소, 만료 시간이 모두 명시되어 있고 프로젝트 표준 용어(tenantId, userId, Redis)를 그대로 사용한다."
    },
    {
      "id": "TUNE-CTL-02",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "검사 대상(readinessProbe), 조건(세 번 연속 실패), 결과(Service 엔드포인트 제외)가 명확하고 프로젝트 표준 용어(Kubernetes, Pod, Service)를 사용한다."
    },
    {
      "id": "TUNE-CTL-03",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체(권한 서비스), 시점(요청마다), 비교 대상(현재 조직 ID와 허용 조직 ID), 조건과 동작(값이 다르면 거부)이 모두 명시되어 있다."
    }
  ]
}
