{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "전달 수단 (API, 파일, DB 등)",
      "suggested_revision": "정산 결과를 다음 단계로 전달할 인터페이스가 필요합니다.",
      "verification_question": "결과를 전달하는 기술적 수단은 무엇입니까?"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "예외 처리 구조 (try-catch, 큐 등)",
      "suggested_revision": "예외를 처리할 오류 핸들러를 둡니다.",
      "verification_question": "예외를 catch 하는 구체적인 모듈은 무엇입니까?"
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "데이터 조회 수단 (API, 속성 등)",
      "suggested_revision": "통계 값을 화면에 표시할 API 엔드포인트를 추가합니다.",
      "verification_question": "데이터를 가져오는 기술적 수단은 무엇입니까?"
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
      "decision": "구체화 필요",
      "reader_must_infer": "가격 계산 순서와 기준",
      "suggested_revision": "기본 가격을 기준으로 개별 상품 할인과 회원 등급 할인을 적용하며, 캠페인 제외 조건은 할인보다 우선합니다.",
      "verification_question": "가격 계산의 시작 기준과 할인 적용 순서가 맞습니까?"
    },
    {
      "id": "DEV-C02",
      "decision": "구체화 필요",
      "reader_must_infer": "판정 우선순위와 기본값",
      "suggested_revision": "승인 여부를 판정할 때 보류 조건이 승인 조건보다 우선하며, 해당 사항이 없으면 기본적으로 거절합니다.",
      "verification_question": "판정 로직의 우선순위와 기본값이 맞습니까?"
    },
    {
      "id": "DEV-C03",
      "decision": "구체화 필요",
      "reader_must_infer": "설정 충돌 해결 규칙",
      "suggested_revision": "알림 설정은 차단 조건이 허용 조건보다 우선하며, 명시된 설정이 없으면 기본적으로 차단합니다.",
      "verification_question": "설정 충돌 시 우선순위 규칙이 맞습니까?"
    },
    {
      "id": "DEV-N01",
      "decision": "구체화 필요",
      "reader_must_infer": "주체와 절차 (누가, 어떻게)",
      "suggested_revision": "월말 마감 이후에는 전표를 수정할 수 없으며, 오류가 발생한 전표는 취소한 후 다시 작성해야 합니다.",
      "verification_question": "수정 불가 주체와 오류 전표 처리 절차가 맞습니까?"
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
