```json
{
  "cases": [
    {
      "id": "TUNE-01",
      "decision": "구체화 필요",
      "suggested_revision": "각 기관의 권한 설정과 공통 역할 설정에서 허용 메뉴를 합쳐 사용자별 유효 메뉴 권한을 만든다.",
      "reason": "tenant와 entitlement snapshot은 문맥에서 기관과 권한 설정으로 뜻이 확정되지만, '머지한다'가 어떤 값을 어떻게 합치는지 대상과 동작을 가린다."
    },
    {
      "id": "TUNE-02",
      "decision": "구체화 필요",
      "suggested_revision": "재고 예약에 실패한 주문을 `inventory-retry` 토픽에 `inventory_retry_requested` 이벤트로 발행한다.",
      "reason": "'재처리 레일에 올린다'는 비유로 실제 동작(이벤트 발행)과 대상 토픽을 가린다."
    },
    {
      "id": "TUNE-03",
      "decision": "구체화 필요",
      "suggested_revision": "업로드 서비스는 모든 행을 먼저 검사하고, 유효한 행만 트랜잭션으로 저장한다.",
      "reason": "주체와 서술어가 빠진 명사 나열로, 검사 주체와 저장 시점을 독자가 추측해야 한다."
    },
    {
      "id": "TUNE-04",
      "decision": "구체화 필요",
      "suggested_revision": "이 분기는 응답하지 않은 문항과 값이 없는 문항을 평균 계산에서 제외한다.",
      "reason": "'통계 왜곡을 막는다'는 평가가 실제 제외 대상과 동작을 대신한다."
    },
    {
      "id": "TUNE-05",
      "decision": "의미 확인 필요",
      "suggested_revision": "정산 배치(`SettlementReconciliationJob`)는 차이 내역을 예외 목록에 추가하고, 원장을 자동 수정하거나 차이를 자동 승인하지 않는다.",
      "reason": "원문의 '클로즈한다'가 차이를 해결한다는 뜻으로 읽히지만, 문맥은 자동 수정이나 자동 승인을 하지 않는다고 명시해 의미가 충돌한다. 자동 종결 여부를 확인해야 한다."
    },
    {
      "id": "TUNE-06",
      "decision": "구체화 필요",
      "suggested_revision": "서버 기동 시 조회 빈도가 높은 상품 5만 건을 Redis에서 로컬 캐시에 사전 적재하면 배포 직후 응답 지연이 줄어든다.",
      "reason": "'데워두는'이 사전 적재 동작을 가리고, '이득이다'가 구체적 효과(p95 감소)를 대신한다."
    },
    {
      "id": "TUNE-07",
      "decision": "구체화 필요",
      "suggested_revision": "세 승인 규칙(approval matrix)을 미리 계산해 사용자별 최종 승인 한도(effective rule)를 저장한다.",
      "reason": "materialize가 미리 계산해 저장한다는 동작을 가리며, 영어 일반어와 한국어 조사의 낯선 결합으로 대상과 동작이 불분명하다."
    },
    {
      "id": "TUNE-08",
      "decision": "구체화 필요",
      "suggested_revision": "권한 서비스는 역할 변경 내역을 `access_role_changed` 이벤트로 `access-audit` 토픽에 발행한다.",
      "reason": "'감사 스트림에 흘린다'는 비유가 실제 발행 동작과 토픽 이름을 가린다."
    },
    {
      "id": "TUNE-09",
      "decision": "구체화 필요",
      "suggested_revision": "서버는 기존 엔드포인트와 필드를 유지하면서 `preferredName` 필드를 선택적으로 추가하고, 신버전 앱만 값이 있을 때 별칭을 표시한다.",
      "reason": "주체와 서술어가 빠진 명사 나열로, 호환 방식의 주체와 새 필드의 사용 조건이 가려졌다."
    },
    {
      "id": "TUNE-10",
      "decision": "구체화 필요",
      "suggested_revision": "마감된 원장의 분개를 직접 수정하면 마감 시점 잔액과 정정 내역을 추적할 수 없으므로, 반대 분개와 정정 분개를 현재 회계 기간에 새로 기록한다.",
      "reason": "'오염시킨다'는 평가가 실제 금지 이유(추적 불가)와 대체 방식(반대 분개 기록)을 대신한다."
    },
    {
      "id": "TUNE-11",
      "decision": "구체화 필요",
      "suggested_revision": "예측 모델은 고객별 이탈 확률을 0부터 1 사이로 계산하고, 분석 서비스는 확률이 0.7 이상인 고객을 상담 검토 목록에 추가한다.",
      "reason": "스코어링, 컷오프, 어플라이 등 음역어가 확률 계산과 임계값 적용이라는 동작을 가린다."
    },
    {
      "id": "TUNE-12",
      "decision": "구체화 필요",
      "suggested_revision": "메뉴 권한과 행 조회 권한을 하나의 세션 값으로 합치면 구현은 단순해지지만, 조직 이동 후 로그아웃 전까지 이전 조직의 행을 조회할 수 있다.",
      "reason": "'한 바구니에 담는다'는 비유가 합치 대상을 가리고, '싸다'는 평가가 구현 단순화와 부작용을 대신한다."
    },
    {
      "id": "TUNE-CTL-01",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "코드 식별자를 보존하면서 캐시 키 형식, 저장소, 만료 시간을 문장 안에서 명확히 제공한다."
    },
    {
      "id": "TUNE-CTL-02",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "표준 용어를 그대로 쓰면서 검사 대상, 조건(세 번 연속 실패), 결과(엔드포인트 제외)를 문장 하나로 명확히 설명한다."
    },
    {
      "id": "TUNE-CTL-03",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체, 검사 시점, 비교값, 조건, 동작이 모두 문장에 들어 있어 독자가 추측할 필요가 없다."
    }
  ]
}
```
