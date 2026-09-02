{
  "cases": [
    {
      "id": "TUNE-01",
      "decision": "구체화 필요",
      "suggested_revision": "권한 서비스는 각 tenant의 entitlement snapshot을 병합한다.",
      "reason": "주체가 명시되지 않아 독자가 동작 주체를 추론해야 함"
    },
    {
      "id": "TUNE-02",
      "decision": "구체화 필요",
      "suggested_revision": "주문 서비스는 실패한 주문을 재처리 워커가 구독하는 `inventory-retry` 토픽에 발행한다.",
      "reason": "‘레일’이라는 비유가 모호하고, 주체·대상·동작이 명확히 제시되지 않음"
    },
    {
      "id": "TUNE-03",
      "decision": "구체화 필요",
      "suggested_revision": "업로드 서비스는 모든 행을 검증한 후에만 데이터를 저장한다.",
      "reason": "명사 나열만으로 주어·동사가 빠져 있어 독자가 의미를 재구성해야 함"
    },
    {
      "id": "TUNE-04",
      "decision": "구체화 필요",
      "suggested_revision": "‘응답하지 않음’ 및 설문 중 이탈 항목을 제외하는 분기는 통계 왜곡을 방지한다.",
      "reason": "‘이 분기’가 무엇을 가리키는지 불명확하고, 평가가 사실을 대신함"
    },
    {
      "id": "TUNE-05",
      "decision": "구체화 필요",
      "suggested_revision": "정산 리컨실리에이션 잡은 차이 내역을 예외 목록에 추가한다.",
      "reason": "‘클로즈한다’가 의미를 명확히 전달하지 못하고, 동작이 모호함"
    },
    {
      "id": "TUNE-06",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "‘캐시를 처음부터 데워두는 것이 이득이다’는 의미가 명확하고 자연스러운 기술 문장"
    },
    {
      "id": "TUNE-07",
      "decision": "구체화 필요",
      "suggested_revision": "권한 서비스는 approval matrix에서 계산된 effective rule을 저장한다.",
      "reason": "영어 동사와 용어 혼용으로 동작이 불명확함"
    },
    {
      "id": "TUNE-08",
      "decision": "구체화 필요",
      "suggested_revision": "권한 서비스는 권한 변경 이벤트를 감사 스트림(`access-audit` 토픽)으로 전송한다.",
      "reason": "‘흘린다’라는 비유가 모호하고, 동작과 대상이 명확히 제시되지 않음"
    },
    {
      "id": "TUNE-09",
      "decision": "구체화 필요",
      "suggested_revision": "기존 API는 그대로 유지하고, 새로운 `preferredName` 필드는 선택적으로 적용한다.",
      "reason": "명사 나열만으로 동작이 드러나지 않아 독자가 의미를 추론해야 함"
    },
    {
      "id": "TUNE-10",
      "decision": "구체화 필요",
      "suggested_revision": "소급 수정은 원장을 오염시키지 않고, 반대 분개와 환불 분개를 추가한다.",
      "reason": "평가가 실제 동작과 반대이며, 동작 설명이 부족함"
    },
    {
      "id": "TUNE-11",
      "decision": "구체화 필요",
      "suggested_revision": "예측 모델은 고객별 이탈 확률을 계산하고, 0.7 이상의 확률에 컷오프를 적용해 상담 검토 목록에 추가한다.",
      "reason": "영어 용어 혼용과 동작 설명이 불명확함"
    },
    {
      "id": "TUNE-12",
      "decision": "구체화 필요",
      "suggested_revision": "모든 권한을 하나의 세션 값에 합치면 구현이 단순해지지만, 조직 이동 후 로그아웃 전까지 이전 행 권한이 남을 위험이 있다.",
      "reason": "‘싸다’라는 비유가 모호하고, 동작·결과가 충분히 서술되지 않음"
    },
    {
      "id": "TUNE-CTL-01",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체·대상·조건·결과가 모두 명시된 명확한 기술 문장"
    },
    {
      "id": "TUNE-CTL-02",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "조건과 결과가 완전하게 서술된 명확한 문장"
    },
    {
      "id": "TUNE-CTL-03",
      "decision": "통과",
      "suggested_revision": null,
      "reason": "주체·시점·비교값·조건·동작이 모두 포함된 완전한 문장"
    }
  ]
}
