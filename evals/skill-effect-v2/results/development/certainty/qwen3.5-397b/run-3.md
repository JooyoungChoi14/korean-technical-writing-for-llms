{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "'다리'에 해당하는 기술적 구현 수단 (API, 큐, 테이블 등)",
      "suggested_revision": "정산 결과를 다음 단계로 전달할 [전달 수단] 이 필요합니다.",
      "verification_question": "정산 결과를 다음 단계로 넘기는 기술적 수단은 무엇입니까?"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "'완충지대'에 해당하는 예외 처리機制 (try-catch, 큐, 테이블 등)",
      "suggested_revision": "예외 발생 시 처리할 [예외 처리 모듈] 을 둡니다.",
      "verification_question": "예외를 구체적으로 어떻게 처리하거나 저장합니까?"
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "'손잡이'에 해당하는 조회 수단 (API 엔드포인트, 함수 등)",
      "suggested_revision": "통계 값을 화면에 표시할 [조회 수단] 을 추가합니다.",
      "verification_question": "통계 값을 가져오는 기술적 수단은 무엇입니까?"
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
      "reader_must_infer": "할인 적용 순서 목록과 제외 조건 우선순위 문구의 모순 관계",
      "suggested_revision": "[확인 필요] 기본 가격을 기준으로 할인을 적용하며, 제외 조건은 할인보다 우선하여 판단합니다.",
      "verification_question": "할인 적용 순서와 제외 조건 판단의 우선순위가 어떻게 됩니까?"
    },
    {
      "id": "DEV-C02",
      "decision": "의미 확인 필요",
      "reader_must_infer": "판정 조건 목록 순서와 보류 우선순위 문구의 모순 관계",
      "suggested_revision": "[확인 필요] 보류 조건을 승인보다 우선하여 판정합니다.",
      "verification_question": "각 판정 조건들의 실제 평가 우선순위는 무엇입니까?"
    },
    {
      "id": "DEV-C03",
      "decision": "의미 확인 필요",
      "reader_must_infer": "허용/차단 조건 목록 순서와 차단 우선순위 문구의 모순 관계",
      "suggested_revision": "[확인 필요] 차단 조건은 허용 조건보다 우선하여 적용합니다.",
      "verification_question": "알림 허용과 차단 조건이 충돌할 때 어떤 규칙으로 최종 상태가 결정됩니까?"
    },
    {
      "id": "DEV-N01",
      "decision": "구체화 필요",
      "reader_must_infer": "주체 (시스템/사용자) 와 동작 (수정 불가, 취소, 재작성) 의 명확한 서술 관계",
      "suggested_revision": "월말 마감 이후에는 전표를 수정할 수 없으며, 오류가 있는 전표는 취소한 후 다시 작성해야 합니다.",
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
