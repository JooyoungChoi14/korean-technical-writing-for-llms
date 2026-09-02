{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "‘다리’가 구체적으로 무엇을 의미하는지(API, 메시지 큐, 테이블 등)와 ‘넘긴다’는 동작의 대상",
      "suggested_revision": "정산 결과를 다음 단계로 전달하는 인터페이스(예: API)가 필요합니다.",
      "verification_question": "‘다리’로 지칭하는 전달 수단은 무엇인가요? (API, 큐, 테이블 등)"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "‘완충지대’가 예외를 처리하는 어떤 메커니즘인지, 예외를 기록·무시·재시도 중 무엇을 하는지",
      "suggested_revision": "예외를 받아서 처리하는 구간을 추가합니다.",
      "verification_question": "‘완충지대’에서 예외를 어떻게 처리하나요? (기록, 무시, 재시도, 별도 저장 등)"
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "‘손잡이’가 통계 값을 화면으로 가져오는 구체적 수단(API, 함수, UI 컨트롤)인지",
      "suggested_revision": "통계 값을 화면에서 조회할 수 있도록 API를 추가합니다.",
      "verification_question": "‘손잡이’는 API, UI 컨트롤, 데이터 전달 함수 중 무엇인가요?"
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
      "reader_must_infer": "‘캠페인 제외’와 ‘기본 가격’이 각각 조건과 기본값이라는 점, ‘순으로 적용’과 ‘제외 조건 우선’의 실제 평가 순서",
      "suggested_revision": "캠페인 제외 조건이 있으면 할인을 적용하지 않고 기본 가격을 사용하며, 제외가 아니면 개별 상품 할인, 회원 등급 할인 순으로 적용합니다.",
      "verification_question": null
    },
    {
      "id": "DEV-C02",
      "decision": "구체화 필요",
      "reader_must_infer": "‘자동 보류’가 승인보다 우선하므로 실제 판정 순서는 보류 조건을 먼저 확인한다는 점",
      "suggested_revision": "자동 보류 조건을 먼저 확인하고, 보류가 아니면 수동 승인, 부서 승인, 기본 거절 순으로 판정합니다.",
      "verification_question": null
    },
    {
      "id": "DEV-C03",
      "decision": "의미 확인 필요",
      "reader_must_infer": "사용자 알림 허용과 채널 허용이 모두 필요한지, 하나만으로 충분한지",
      "suggested_revision": null,
      "verification_question": "사용자 알림 허용과 채널 허용이 모두 충족되어야 알림을 보내나요, 아니면 하나만 충족되어도 되나요?"
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
