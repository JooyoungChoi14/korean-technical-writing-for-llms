{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "의미 확인 필요",
      "reader_must_infer": "전달 메커니즘 (API, 파일 적재, 메시지 큐 등)",
      "suggested_revision": "정산 결과를 다음 단계로 전달할 [전달 수단] 이 필요합니다.",
      "verification_question": "정산 결과를 다음 단계로 넘기는 구체적인 기술 수단은 무엇입니까?"
    },
    {
      "id": "DEV-A02",
      "decision": "의미 확인 필요",
      "reader_must_infer": "예외 처리 구조 (try-catch, 데드 레터 큐, 재시도 로직 등)",
      "suggested_revision": "예외를 처리할 [예외 처리 구조] 를 마련합니다.",
      "verification_question": "예외를 받아내는 구체적인 구조는 무엇입니까?"
    },
    {
      "id": "DEV-A03",
      "decision": "의미 확인 필요",
      "reader_must_infer": "데이터 노출 수단 (API 엔드포인트, 컴포넌트 속성, 버튼 동작 등)",
      "suggested_revision": "통계 값을 화면에 표시할 [데이터 노출 수단] 을 추가합니다.",
      "verification_question": "통계 값을 화면으로 가져오는 구체적인 수단은 무엇입니까?"
    },
    {
      "id": "DEV-P01",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "DEV-P02",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "DEV-P03",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "DEV-C01",
      "decision": "의미 확인 필요",
      "reader_must_infer": "계산 순서와 기본 가격의 역할 (시작 값인지 적용 단계인지)",
      "suggested_revision": "기본 가격을 기준으로 [할인 적용 순서] 를 적용하며 제외 조건은 할인보다 우선합니다.",
      "verification_question": "계산 순서에서'기본 가격'은 시작 값입니까, 아니면 적용 단계 중 하나입니까?"
    },
    {
      "id": "DEV-C02",
      "decision": "의미 확인 필요",
      "reader_must_infer": "판정 로직의 우선순위와 순차 처리 관계",
      "suggested_revision": "판정 조건에 따라 [상태] 중 하나를 선택하며 보류 조건이 충족되면 승인보다 우선합니다.",
      "verification_question": "나열된 항목은 처리 순서입니까, 아니면 우선순위 평가 목록입니까?"
    },
    {
      "id": "DEV-C03",
      "decision": "의미 확인 필요",
      "reader_must_infer": "우선순위 규칙과 목록 순서의 관계",
      "suggested_revision": "[알림 정책] 을 적용하며 차단 조건이 충족되면 항상 우선합니다.",
      "verification_question": "'차단 우선'규칙이 목록 순서보다 우선합니까?"
    },
    {
      "id": "DEV-N01",
      "decision": "구체화 필요",
      "reader_must_infer": "주체 (시스템 또는 사용자) 및 조건 (어떤 오류인지)",
      "suggested_revision": "월말 마감 이후에는 전표를 수정할 수 없으며, 오류가 발생한 전표는 취소한 후 다시 작성해야 합니다.",
      "verification_question": null
    },
    {
      "id": "DEV-P04",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "DEV-P05",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    }
  ]
}
