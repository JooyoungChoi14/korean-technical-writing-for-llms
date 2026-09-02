{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "'다리'가 의미하는 기술적 구성 요소 (API, 파이프라인 등)",
      "suggested_revision": "정산 결과를 다음 단계로 전달할 인터페이스 (또는 파이프라인) 가 필요합니다.",
      "verification_question": "'다리'가 구체적으로 어떤 기술 구성 요소를 의미합니까?"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "'완충지대'가 의미하는 예외 처리 메커니즘",
      "suggested_revision": "예외 발생 시 처리할 오류 핸들링 로직 (또는 재시도 큐) 을 구현합니다.",
      "verification_question": "'완충지대'가 구체적으로 어떤 예외 처리 메커니즘을 의미합니까?"
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "'손잡이'가 의미하는 UI 요소 또는 기능",
      "suggested_revision": "통계 값을 화면에 표시하도록 요청할 수 있는 UI 컨트롤 (또는 API 파라미터) 을 추가합니다.",
      "verification_question": "'손잡이'가 구체적으로 어떤 UI 요소 또는 기능적 접점을 의미합니까?"
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
      "reader_must_infer": "할인 적용 순서와 기본 가격 산정 시점의 논리적 관계",
      "suggested_revision": "기본 가격을 기준으로 캠페인 제외 조건을 먼저 확인한 후, 개별 상품 할인 및 회원 등급 할인을 순차적으로 적용합니다.",
      "verification_question": "할인 적용 순서가 기본 가격보다 먼저 명시된 것이 의도된 사항입니까?"
    },
    {
      "id": "DEV-C02",
      "decision": "의미 확인 필요",
      "reader_must_infer": "승인 판정 로직의 우선순위와 순서의 관계",
      "suggested_revision": "승인 판정 시 보류 조건이 충족되면 우선 보류 처리하며, 그 외 경우 부서 승인 또는 수동 승인을 거쳐 기본 거절 여부를 확정합니다.",
      "verification_question": "'기본 거절'이 순서의 마지막에 오는 것이 맞습니까? 우선순위 규칙과 상태 전이 로직을 명확히 해야 합니다."
    },
    {
      "id": "DEV-C03",
      "decision": "의미 확인 필요",
      "reader_must_infer": "차단 우선 규칙과 적용 순서 간의 모순",
      "suggested_revision": "알림 설정은 차단 규칙이 허용 규칙보다 우선하며, 조직 수준 차단이 사용자 수준 허용보다 우선합니다.",
      "verification_question": "'차단을 항상 우선'한다는 규칙과 나열된 적용 순서 간의 모순을 해결해야 합니다. 어떤 규칙이 최우선입니까?"
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
