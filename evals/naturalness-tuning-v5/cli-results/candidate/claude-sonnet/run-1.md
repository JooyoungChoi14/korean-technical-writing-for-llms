{
  "cases": [
    {
      "id": "TUNE-01",
      "decision": "구체화 필요",
      "suggested_revision": "권한 서비스는 사용자가 속한 기관의 권한 설정과 공통 역할 설정을 읽고, 두 설정에 포함된 허용 메뉴를 합친다.",
      "reason": "tenant와 entitlement snapshot이라는 영어 전문 용어가 문맥에서 이미 정의된 '기관'과 '권한 설정'을 대신하고 있으며, 'merge'를 음역한 '머지'가 실제 동작인 '합친다'를 가린다."
    },
    {
      "id": "TUNE-02",
      "decision": "구체화 필요",
      "suggested_revision": "주문 서비스는 실패한 주문을 `inventory-retry` 토픽에 발행한다.",
      "reason": "'재처리 레일에 올린다'는 비유가 실제 동작인 Kafka 토픽 발행을 대신한다. 문맥에서 발행 작업을 설명한다고 명시했으므로 구체적인 동작을 노출해야 한다."
    },
    {
      "id": "TUNE-03",
      "decision": "구체화 필요",
      "suggested_revision": "모든 행을 검증한 뒤 유효할 때만 저장한다.",
      "reason": "명사 나열('검증 선행, 반영 후속')로 서술어가 생략되어 독자가 주체와 동작을 추측해야 한다."
    },
    {
      "id": "TUNE-04",
      "decision": "구체화 필요",
      "suggested_revision": "이 조건문은 값이 없는 문항을 평균 계산에서 제외해 통계가 왜곡되지 않게 한다.",
      "reason": "'통계 왜곡을 막는다'는 평가가 실제 동작(값의 존재 확인 후 제외)과 그 결과(평균 계산 정확성)를 대신한다."
    },
    {
      "id": "TUNE-05",
      "decision": "구체화 필요",
      "suggested_revision": "정산 대조 배치(`SettlementReconciliationJob`)가 차이 내역을 예외 목록에 추가한다.",
      "reason": "'리컨실리에이션'은 한국어 '대조'로, '클로즈'는 문맥의 실제 동작인 '예외 목록에 추가'로 바꾸어야 한다. 문맥은 자동 수정이나 승인을 명시적으로 부정한다."
    },
    {
      "id": "TUNE-06",
      "decision": "구체화 필요",
      "suggested_revision": "서버 기동 시 로컬 캐시에 상위 5만 건을 미리 적재하면 배포 직후 검색 응답 지연이 줄어든다.",
      "reason": "'데워둔다', '이득'이라는 비유와 평가가 실제 동작(미리 적재)과 측정 가능한 결과(지연 감소)를 대신한다."
    },
    {
      "id": "TUNE-07",
      "decision": "구체화 필요",
      "suggested_revision": "권한 서비스는 세 규칙을 미리 계산해 사용자별 최종 승인 한도를 저장한다.",
      "reason": "'approval matrix', 'effective rule', 'materialize'가 문맥에서 정의된 '세 규칙', '최종 승인 한도', '미리 계산해 저장'을 대신한다."
    },
    {
      "id": "TUNE-08",
      "decision": "구체화 필요",
      "suggested_revision": "권한 서비스는 역할 변경 이벤트를 `access-audit` 토픽에 발행한다.",
      "reason": "'감사 스트림에 흘린다'는 비유가 실제 동작인 Kafka 토픽 발행을 대신한다."
    },
    {
      "id": "TUNE-09",
      "decision": "구체화 필요",
      "suggested_revision": "기존 엔드포인트와 필드를 유지하고, 신버전 앱에서만 사용하는 `preferredName` 필드를 추가한다.",
      "reason": "명사 나열('기존 API 유지, 신규 필드 선택 적용')로 서술어가 생략되어 독자가 주체와 동작을 추측해야 한다."
    },
    {
      "id": "TUNE-10",
      "decision": "구체화 필요",
      "suggested_revision": "마감 후 원장 수정은 과거 분개를 그대로 두고 현재 기간에 정정 분개를 추가하는 방식으로만 가능하다.",
      "reason": "'소급 수정은 원장을 오염시킨다'는 평가가 실제 규칙(마감 후 수정 금지, 정정 분개 추가)을 대신한다. 문맥은 '오염 방지'가 아니라 '추적 가능성'을 목표로 명시한다."
    },
    {
      "id": "TUNE-11",
      "decision": "구체화 필요",
      "suggested_revision": "분석 서비스는 모델이 계산한 이탈 확률이 0.7 이상인 고객을 상담 검토 목록에 추가한다.",
      "reason": "'세그먼트 스코어링', '컷오프 어플라이'가 실제 동작(확률 계산, 임계값 비교, 목록 추가)을 대신한다. 문맥은 세그먼트를 새로 나누지 않는다고 명시한다."
    },
    {
      "id": "TUNE-12",
      "decision": "구체화 필요",
      "suggested_revision": "메뉴 권한과 행 조회 권한을 하나의 세션 값으로 합치면 조직 이동 뒤 로그아웃할 때까지 이전 행을 볼 수 있다.",
      "reason": "'한 바구니에 담으면 싸다'는 비유가 실제 문제(조직 이동 후 권한 불일치)를 대신한다."
    },
    {
      "id": "TUNE-CTL-01",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "코드에서 사용하는 식별자, 저장소, 형식, 만료 시간이 모두 명시되어 독자가 추가 정보를 추측할 필요가 없다."
    },
    {
      "id": "TUNE-CTL-02",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체(Kubernetes readinessProbe), 조건(세 번 연속 실패), 결과(Service 엔드포인트에서 제외)가 모두 명시되어 있으며, 용어집에서 정의된 표준 용어를 사용한다."
    },
    {
      "id": "TUNE-CTL-03",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체(권한 서비스), 검사 시점(요청 시), 비교 대상(현재 조직 ID와 허용 조직 ID), 조건과 결과(다르면 거부)가 모두 명시되어 독자가 추가 정보를 추측할 필요가 없다."
    }
  ]
}
