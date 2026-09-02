{
  "cases": [
    {
      "id": "TUNE-01",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "문맥에서 tenant와 entitlement snapshot의 의미가 명확히 정의되었고, 'merge'는 두 설정을 합치는 동작으로 충분히 이해된다."
    },
    {
      "id": "TUNE-02",
      "decision": "구체화 필요",
      "suggested_revision": "실패한 주문을 재처리 큐에 보낸다.",
      "reason": "'레일'은 비유적 표현이며, 문맥의 실제 동작(이벤트 발행, Kafka 토픽)을 더 직접적으로 나타내야 한다."
    },
    {
      "id": "TUNE-03",
      "decision": "구체화 필요",
      "suggested_revision": "검증 후 저장.",
      "reason": "명사 나열로 동작의 주체와 대상이 불명확하다. 누가 무엇을 하는지 최소한의 동사형으로 나타내야 한다."
    },
    {
      "id": "TUNE-04",
      "decision": "구체화 필요",
      "suggested_revision": "이 분기는 응답 없는 항목과 이탈한 항목을 통계에서 제외해 평균을 정확히 계산한다.",
      "reason": "'왜곡'은 판단으로 실제 효과를 대신한다. 무엇을 제외하고 어떤 결과를 얻는지 명시해야 한다."
    },
    {
      "id": "TUNE-05",
      "decision": "의미 확인 필요",
      "suggested_revision": null,
      "reason": "'클로즈'는 차이 항목을 예외 목록에 추가하는 것인지, 결과 보고인지 원문만으로 확정되지 않는다. 질문: 배치가 실제로 수행하는 동작이 무엇인가?"
    },
    {
      "id": "TUNE-06",
      "decision": "구체화 필요",
      "suggested_revision": "배포 직후 응답 지연을 줄이려면 캐시를 미리 적재하는 것이 메모리 추가 사용보다 효율적이다.",
      "reason": "'데운다'는 비유이고, '이득'은 판단이다. 메모리 비용과 성능 개선을 정량적으로 비교한 이유를 명시해야 한다."
    },
    {
      "id": "TUNE-07",
      "decision": "구체화 필요",
      "suggested_revision": "세 규칙을 미리 계산해 사용자별 최종 승인 한도를 저장한다.",
      "reason": "'materialize'는 코드 용어로, 문맥의 실제 동작(계산과 저장)을 한국어로 설명해야 한다."
    },
    {
      "id": "TUNE-08",
      "decision": "구체화 필요",
      "suggested_revision": "권한 변경 이벤트를 감사 토픽에 발행한다.",
      "reason": "'흘린다'는 비유적 표현이다. 문맥에서 명시된 실제 동작(발행, Kafka 토픽)을 직접 나타내야 한다."
    },
    {
      "id": "TUNE-09",
      "decision": "구체화 필요",
      "suggested_revision": "기존 API와 필드를 유지하고 새로운 선택 필드를 추가한다.",
      "reason": "명사 나열로 누가 무엇을 하는지 불명확하다. 서버의 동작을 동사형으로 명시해야 한다."
    },
    {
      "id": "TUNE-10",
      "decision": "구체화 필요",
      "suggested_revision": "월 마감 후 정정을 원장에 추가하면 마감 시점의 잔액과 이후 변경 내역이 모두 기록된다.",
      "reason": "'오염'은 판단으로 실제 효과(추적 기능)를 대신한다. 이 방식이 보존하는 정보를 명시해야 한다."
    },
    {
      "id": "TUNE-11",
      "decision": "구체화 필요",
      "suggested_revision": "모델이 고객별 이탈 확률을 계산하고, 0.7 이상인 고객을 상담 목록에 추가한다.",
      "reason": "'세그먼트를 스코어링', '컷오프를 어플라이' 같은 기술 용어 나열이 독자가 추측해야 할 정보를 늘린다. 구체적인 계산과 동작을 설명해야 한다."
    },
    {
      "id": "TUNE-12",
      "decision": "구체화 필요",
      "suggested_revision": "두 권한을 한 세션 값으로 합치면 구현은 단순하지만, 조직 이동 후 로그아웃할 때까지 이전 데이터를 볼 수 있는 문제가 생긴다.",
      "reason": "'싸다'는 비유이고 '모든 권한을 한 바구니'도 은유다. 실제 단점(조직 이동 후 동기화 지연)을 명시해야 한다."
    },
    {
      "id": "TUNE-CTL-01",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "식별자, 저장소, 만료 시간이 모두 명시되어 있고, 실제 코드 이름을 사용해 명확하다."
    },
    {
      "id": "TUNE-CTL-02",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "Kubernetes 표준 용어를 유지하면서 검사 대상(readinessProbe), 조건(세 번 연속 실패), 결과(제외)를 모두 명시한다."
    },
    {
      "id": "TUNE-CTL-03",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체(권한 서비스), 시점(요청마다), 비교값(현재/허용 조직 ID), 조건(다름), 동작(거부)이 모두 명확하다."
    }
  ]
}
