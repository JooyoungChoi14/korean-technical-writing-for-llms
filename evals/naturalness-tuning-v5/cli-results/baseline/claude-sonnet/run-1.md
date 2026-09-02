{
  "cases": [
    {
      "id": "TUNE-01",
      "decision": "구체화 필요",
      "suggested_revision": "세 기관의 권한 설정과 공통 역할 설정에서 허용된 메뉴를 합친다.",
      "reason": "tenant와 entitlement snapshot이라는 영어 용어가 동작(머지)을 가리며, 실제 대상(기관별 권한 설정)과 동작(메뉴 허용 목록 합치기)이 문맥에만 있다."
    },
    {
      "id": "TUNE-02",
      "decision": "구체화 필요",
      "suggested_revision": "실패한 주문의 재처리 요청 이벤트를 Kafka 토픽에 발행한다.",
      "reason": "레일에 올린다는 비유가 실제 동작(이벤트 발행)을 가리며, 독자는 문맥에서 Kafka 토픽 발행을 복원해야 한다."
    },
    {
      "id": "TUNE-03",
      "decision": "구체화 필요",
      "suggested_revision": "모든 행을 검증한 뒤 유효할 때만 데이터베이스에 저장한다.",
      "reason": "검증 선행, 반영 후속이라는 압축된 명사가 주체(서비스), 검사 조건(모든 행 유효), 저장 동작을 생략한다."
    },
    {
      "id": "TUNE-04",
      "decision": "구체화 필요",
      "suggested_revision": "이 조건문은 응답하지 않음을 선택한 문항과 이탈로 값이 없는 문항을 평균 계산에서 제외한다.",
      "reason": "통계 왜곡을 막는다는 평가가 실제 동작(특정 문항 제외)과 조건(응답 없음, 이탈)을 대신한다."
    },
    {
      "id": "TUNE-05",
      "decision": "구체화 필요",
      "suggested_revision": "정산 대조 배치(`SettlementReconciliationJob`)가 차이 내역을 예외 목록에 추가한다.",
      "reason": "리컨실리에이션 잡과 클로즈라는 음역어가 실제 동작(예외 목록 추가)을 가리며, 문맥에서 배치가 자동 수정하지 않는다는 정보가 빠진다."
    },
    {
      "id": "TUNE-06",
      "decision": "구체화 필요",
      "suggested_revision": "서버 기동 시 자주 조회하는 상품을 로컬 캐시에 미리 적재하면 배포 직후 검색 지연이 줄어든다.",
      "reason": "데워두는 편이 이득이라는 평가가 실제 조건(서버 기동 시 사전 적재), 동작(로컬 캐시), 결과(지연 감소)를 대신한다."
    },
    {
      "id": "TUNE-07",
      "decision": "구체화 필요",
      "suggested_revision": "직급, 부서, 사용자별 규칙을 미리 계산해 사용자별 최종 승인 한도를 저장한다.",
      "reason": "approval matrix, effective rule, materialize라는 영어 용어가 실제 대상(세 규칙)과 동작(미리 계산해 저장)을 가린다."
    },
    {
      "id": "TUNE-08",
      "decision": "구체화 필요",
      "suggested_revision": "권한 변경 이벤트를 Kafka의 감사 토픽에 발행한다.",
      "reason": "감사 스트림에 흘린다는 비유가 실제 동작(Kafka 토픽 발행)을 가리며, 독자는 문맥에서 발행 대상을 복원해야 한다."
    },
    {
      "id": "TUNE-09",
      "decision": "구체화 필요",
      "suggested_revision": "기존 엔드포인트와 필드를 유지하면서 선택 필드 `preferredName`을 추가한다. 신버전 앱만 값이 있을 때 별칭을 표시한다.",
      "reason": "기존 API 유지, 신규 필드 선택 적용이라는 압축된 명사가 주체(서버), 동작(필드 추가), 조건(값 있을 때)을 생략한다."
    },
    {
      "id": "TUNE-10",
      "decision": "구체화 필요",
      "suggested_revision": "마감 뒤 원장을 수정하면 마감 당시 잔액을 추적할 수 없다.",
      "reason": "소급 수정이 원장을 오염시킨다는 평가가 실제 위험(마감 잔액 추적 불가)과 조건(마감 뒤)을 대신한다."
    },
    {
      "id": "TUNE-11",
      "decision": "구체화 필요",
      "suggested_revision": "예측 모델이 고객별 이탈 확률을 계산하고, 분석 서비스가 확률 0.7 이상인 고객을 상담 검토 목록에 추가한다.",
      "reason": "세그먼트 스코어링, 컷오프 어플라이라는 영어 용어가 실제 주체(모델과 서비스), 동작(확률 계산, 목록 추가), 조건(0.7 이상)을 가린다."
    },
    {
      "id": "TUNE-12",
      "decision": "구체화 필요",
      "suggested_revision": "메뉴 권한과 행 조회 권한을 세션에 함께 저장하면 구현은 단순해지지만 조직 이동 뒤 로그아웃 전까지 이전 행을 볼 수 있다.",
      "reason": "한 바구니에 담으면 싸다는 비유가 실제 위험(조직 이동 뒤 권한 불일치)과 조건(로그아웃 전까지)을 대신한다."
    },
    {
      "id": "TUNE-CTL-01",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체(캐시 키), 동작(만들고 저장), 대상(Redis), 조건(형식과 만료 시간)이 모두 명시되어 있다."
    },
    {
      "id": "TUNE-CTL-02",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체(readinessProbe), 검사 조건(세 번 연속 실패), 동작(제외), 대상(Service 엔드포인트)이 모두 명시되어 있다. 문맥에서 이들 용어가 프로젝트 표준임이 확인된다."
    },
    {
      "id": "TUNE-CTL-03",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체(권한 서비스), 검사 시점(요청마다), 비교 대상(두 ID), 조건(값이 다름), 결과(조회 거부)가 모두 명시되어 있다."
    }
  ]
}
