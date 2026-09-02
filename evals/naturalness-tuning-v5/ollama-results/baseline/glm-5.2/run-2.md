```json
{
  "cases": [
    {
      "id": "TUNE-01",
      "decision": "구체화 필요",
      "suggested_revision": "각 기관의 권한 설정과 공통 역할 설정에서 허용 메뉴를 합쳐 사용자별 유효 메뉴 권한을 만든다.",
      "reason": "tenant, entitlement snapshot, 머지가 영어 일반어·음역어·약칭으로 결합되어 있고, 실제 동작(허용 메뉴 합산)이 드러나지 않는다."
    },
    {
      "id": "TUNE-02",
      "decision": "구체화 필요",
      "suggested_revision": "재고 예약에 실패한 주문을 `inventory-retry` 토픽에 발행한다.",
      "reason": "재처리 레일에 올린다는 비유가 발행 작업이라는 실제 동작을 대신하며, 토픔명이 빠져 있다."
    },
    {
      "id": "TUNE-03",
      "decision": "구체화 필요",
      "suggested_revision": "업로드 서비스는 모든 행을 먼저 검사하고, 유효한 행만 트랜잭션으로 저장한다.",
      "reason": "명사 나열로 주체와 서술어가 빠져 있어 검사 주체와 저장 조건을 독자가 추측해야 한다."
    },
    {
      "id": "TUNE-04",
      "decision": "구체화 필요",
      "suggested_revision": "이 분기는 응답하지 않은 문항과 값이 없는 문항을 평균 계산에서 제외한다.",
      "reason": "통계 왜곡을 막는다는 평가가 실제 동작(누락·이탈 문항 제외)을 대신한다."
    },
    {
      "id": "TUNE-05",
      "decision": "구체화 필요",
      "suggested_revision": "정산 배치는 차이 내역을 예외 목록에 추가하고 자동으로 수정하거나 승인하지 않는다.",
      "reason": "리컨실리에이션 잡, 클로즈한다가 음역어·비유이며, 클로즈한다는 자동 해결을 암시해 원문의 자동 수정 금지와 모순된다."
    },
    {
      "id": "TUNE-06",
      "decision": "구체화 필요",
      "suggested_revision": "조회 빈도가 높은 상품을 서버 기동 시 로컬 캐시에 미리 적재하면 응답 지연이 줄어들어 추가 메모리 사용보다 이득이다.",
      "reason": "데워두는 편이 이득이다가 비유와 평가로만 결론을 전달하며, 구체적 동작(사전 적재)과 근거(p95 개선)가 드러나지 않는다."
    },
    {
      "id": "TUNE-07",
      "decision": "구체화 필요",
      "suggested_revision": "세 규칙을 미리 계산해 사용자별 최종 승인 한도를 저장한다.",
      "reason": "approval matrix, effective rule, materialize가 영어 일반어와 음역어로 결합되어 있고, 실제 동작(미리 계산해 저장)이 가려져 있다."
    },
    {
      "id": "TUNE-08",
      "decision": "구체화 필요",
      "suggested_revision": "권한 변경 이벤트를 `access-audit` 토픽에 발행한다.",
      "reason": "감사 스트림에 흘린다는 비유가 토픽 발행이라는 동작을 대신하며, 토픽명이 빠져 있다."
    },
    {
      "id": "TUNE-09",
      "decision": "구체화 필요",
      "suggested_revision": "기존 엔드포인트와 필드를 유지하고, `preferredName` 필드를 선택으로 추가한다.",
      "reason": "명사 나열로 서술어가 빠져 있어 유지 대상과 추가 방식이 구체적으로 드러나지 않는다."
    },
    {
      "id": "TUNE-10",
      "decision": "구체화 필요",
      "suggested_revision": "마감된 원장을 소급 수정하면 마감 시점 잔액과 정정 내역을 추적할 수 없다.",
      "reason": "오염시킨다는 평가가 실제 이유(마감 잔액과 정정 내역 추적 불가)를 대신한다."
    },
    {
      "id": "TUNE-11",
      "decision": "구체화 필요",
      "suggested_revision": "예측 모델이 고객별 이탈 확률을 계산하고, 확률이 0.7 이상인 고객을 상담 검토 목록에 추가한다.",
      "reason": "세그먼트 스코어링, 컷오프 어플라이가 영어 일반어·음역어로 결합되어 있고, 실제 동작(확률 계산·임계값 적용)이 가려져 있다."
    },
    {
      "id": "TUNE-12",
      "decision": "구체화 필요",
      "suggested_revision": "메뉴 권한과 행 조회 권한을 하나의 세션 값으로 합치면 구현은 단순해지지만 조직 이동 후 이전 행을 볼 수 있다.",
      "reason": "바구니에 담으면 싸다는 비유와 평가가 실제 문제(구현 단순화 vs 조직 이동 후 권한 갱신 누락)를 대신한다."
    },
    {
      "id": "TUNE-CTL-01",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "코드 식별자를 유지하면서 캐시 키 형식, 저장소, 만료 시간을 명확히 서술한다."
    },
    {
      "id": "TUNE-CTL-02",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "표준 용어를 유지하면서 검사 대상, 조건(세 번 연속 실패), 결과(Pod 제외)를 모두 명시한다."
    },
    {
      "id": "TUNE-CTL-03",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체, 검사 시점, 비교값, 조건, 동작이 모두 명확하게 서술되어 있다."
    }
  ]
}
```
