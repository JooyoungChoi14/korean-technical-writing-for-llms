{
  "cases": [
    {
      "id": "TUNE-01",
      "decision": "구체화 필요",
      "suggested_revision": "세 기관의 권한 설정과 공통 역할 설정에서 허용된 메뉴를 합친다.",
      "reason": "merge와 snapshot이 무엇을 뜻하는지 독자가 이미 알고 있어야 함. 실제 동작(설정 읽기, 메뉴 합치기)이 표현에 드러나지 않음"
    },
    {
      "id": "TUNE-02",
      "decision": "구체화 필요",
      "suggested_revision": "`inventory_retry_requested` 이벤트를 `inventory-retry` 토픽에 발행한다.",
      "reason": "레일에 올린다는 비유가 실제 동작(이벤트 발행, 토픽 전달)을 가림. 문맥에 제시된 구체적 메커니즘을 그대로 쓰는 것이 명확함"
    },
    {
      "id": "TUNE-03",
      "decision": "구체화 필요",
      "suggested_revision": "모든 행을 검증한 뒤 유효할 때만 저장한다.",
      "reason": "선행/후속이라는 압축 표현이 조건(모든 행 유효)과 동작(저장)을 생략함. 독자가 조사를 채워야 함"
    },
    {
      "id": "TUNE-04",
      "decision": "구체화 필요",
      "suggested_revision": "값이 없는 문항을 평균 계산에서 제외한다.",
      "reason": "왜곡을 막는다는 평가가 실제 동작(제외)과 대상(값 없는 문항)을 대신함. 무엇을 어떻게 처리하는지가 드러나지 않음"
    },
    {
      "id": "TUNE-05",
      "decision": "구체화 필요",
      "suggested_revision": "정산 대조 작업(`SettlementReconciliationJob`)이 차이 내역을 예외 목록에 추가한다.",
      "reason": "리컨실리에이션을 아는 독자에게도 클로즈가 자동 승인인지 담당자 확인 대기인지 불명확. 문맥의 실제 동작(목록 추가)을 써야 함"
    },
    {
      "id": "TUNE-06",
      "decision": "구체화 필요",
      "suggested_revision": "서버 기동 시 상품 5만 건을 로컬 캐시에 미리 적재하면 배포 직후 검색 지연이 줄어든다.",
      "reason": "이득이라는 평가가 조건(기동 시 적재), 결과(지연 감소), 트레이드오프(메모리 증가)를 생략함"
    },
    {
      "id": "TUNE-07",
      "decision": "구체화 필요",
      "suggested_revision": "세 규칙을 계산해 사용자별 최종 승인 한도를 저장한다.",
      "reason": "approval matrix, effective rule, materialize 모두 음역어/전문어로 대상(세 규칙)과 동작(계산 후 저장)을 가림"
    },
    {
      "id": "TUNE-08",
      "decision": "구체화 필요",
      "suggested_revision": "권한 변경 이벤트를 `access-audit` 토픽에 발행한다.",
      "reason": "흘린다는 비유가 실제 동작(발행)과 목적지(토픽)를 가림. 문맥에 제시된 구체적 메커니즘을 쓰는 것이 명확함"
    },
    {
      "id": "TUNE-09",
      "decision": "구체화 필요",
      "suggested_revision": "엔드포인트와 기존 필드를 유지하고 선택 필드 `preferredName`을 추가한다.",
      "reason": "압축된 명사 나열이 주어(서버)와 동작(유지, 추가)을 생략함. 독자가 조사를 채워야 함"
    },
    {
      "id": "TUNE-10",
      "decision": "구체화 필요",
      "suggested_revision": "마감 후 수정은 원래 분개를 변경하지 않고 새 분개를 추가한다.",
      "reason": "오염이라는 평가가 실제 방식(변경 금지, 새 분개 추가)과 근거(마감 잔액과 정정 추적)를 대신함"
    },
    {
      "id": "TUNE-11",
      "decision": "구체화 필요",
      "suggested_revision": "모델이 고객별 이탈 확률을 계산하고 0.7 이상인 고객을 검토 목록에 추가한다.",
      "reason": "스코어링, 세그먼트, 컷오프, 어플라이 모두 음역어로 대상(고객)과 동작(확률 계산, 목록 추가)을 가림"
    },
    {
      "id": "TUNE-12",
      "decision": "구체화 필요",
      "suggested_revision": "메뉴 권한과 행 조회 권한을 하나로 합치면 조직 이동 뒤 이전 행을 볼 수 있다.",
      "reason": "싸다는 평가가 조건(합침)과 실제 문제(조직 이동 시 권한 불일치)를 대신함"
    },
    {
      "id": "TUNE-CTL-01",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "식별자 이름, 형식, 저장소, 만료 시간이 모두 명시됨. 코드 식별자를 그대로 쓰는 것이 프로젝트 문맥에서 적절함"
    },
    {
      "id": "TUNE-CTL-02",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "검사 대상(readinessProbe), 조건(세 번 연속 실패), 결과(Service 엔드포인트 제외)가 모두 드러남. 확립된 Kubernetes 용어를 그대로 쓰는 것이 적절함"
    },
    {
      "id": "TUNE-CTL-03",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체(권한 서비스), 시점(요청마다), 비교 대상(두 조직 ID), 조건(다름), 동작(거부)이 모두 명시됨"
    }
  ]
}
