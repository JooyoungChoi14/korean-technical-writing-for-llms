{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "‘다리’가 무엇을 연결하는지, 어떤 동작(전달, 변환, 저장)을 의미하는지",
      "suggested_revision": "정산 결과를 다음 단계로 전달하는 인터페이스를 추가합니다.",
      "verification_question": "‘다리’가 실제로 어떤 구성 요소(함수, API, 메시지 큐 등)를 의미합니까?"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "‘완충지대’가 예외를 어떻게 처리하는지(잡아서 기록, 무시, 재시도 등)",
      "suggested_revision": "예외를 포착하여 기록하고 처리를 계속할 수 있는 구간을 둡니다.",
      "verification_question": "예외를 받아낸 후 어떤 동작을 수행합니까? (로깅, 무시, 재시도 등)"
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "‘손잡이’가 어떤 API나 속성을 통해 통계 값을 화면에 전달하는지",
      "suggested_revision": "통계 값을 화면에 표시할 수 있도록 조회 API를 추가합니다.",
      "verification_question": "통계 값을 화면으로 전달하는 구체적인 방법(API, 웹소켓, 파일 등)은 무엇입니까?"
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
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "DEV-C02",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "DEV-C03",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "DEV-N01",
      "decision": "구체화 필요",
      "reader_must_infer": "주어와 동작이 생략되어 누가 전표를 수정/취소하는지, ‘불가’의 조건이 명확하지 않음",
      "suggested_revision": "월말 마감 이후에는 전표를 수정할 수 없으며, 오류 전표는 취소 후 재작성해야 합니다.",
      "verification_question": "이 규칙의 적용 대상(사용자, 시스템)과 예외 조건이 있습니까?"
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
