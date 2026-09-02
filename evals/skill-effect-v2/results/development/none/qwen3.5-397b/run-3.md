{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "\"다리\"가 의미하는 기술적 연결 수단",
      "suggested_revision": "정산 결과를 다음 단계로 전달할 인터페이스가 필요합니다.",
      "verification_question": "\"다리\"가 API, 메시지 큐, DB 테이블 중 무엇을 의미합니까?"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "\"완충지대\"의 구현 방식",
      "suggested_revision": "예외 발생 시 처리를 위한 오류 핸들링 계층을 둡니다.",
      "verification_question": "\"완충지대\"가 재시도 로직인지 오류 로그 저장소인지 명확히 해야 합니다."
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "\"손잡이\"의 실제 기능",
      "suggested_revision": "통계 값을 화면에 조회할 수 있는 기능을 추가합니다.",
      "verification_question": "\"손잡이\"가 UI 버튼입니까 백엔드 API 입니까?"
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
      "reader_must_infer": "할인 적용 계산 로직의 실제 순서",
      "suggested_revision": "기본 가격을 기준으로 캠페인 제외 여부를 확인한 후 할인을 적용합니다.",
      "verification_question": "\"기본 가격 순으로 적용\"이라는 표현이 할인 적용 순서에서 마지막 단계를 의미합니까?"
    },
    {
      "id": "DEV-C02",
      "decision": "의미 확인 필요",
      "reader_must_infer": "승인 판정 규칙의 우선순위와 처리 순서 관계",
      "suggested_revision": "판정 우선순위는 보류 > 승인 > 거절이며, 자동 보류 조건이 충족되면 다른 승인 조건보다 우선합니다.",
      "verification_question": "나열된 순서가 처리 순서입니까 우선순위입니까? 우선순위 규칙과 모순되지 않습니까?"
    },
    {
      "id": "DEV-C03",
      "decision": "의미 확인 필요",
      "reader_must_infer": "차단 우선 규칙과 설정 순서의 충돌 관계",
      "suggested_revision": "알림 설정 우선순위는 차단 > 허용이며, 조직 수준 차단은 사용자 수준 허용보다 우선합니다.",
      "verification_question": "\"차단을 항상 우선합니다\"가 사용자 허용 설정보다 우선한다는 것이 맞습니까?"
    },
    {
      "id": "DEV-N01",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
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
