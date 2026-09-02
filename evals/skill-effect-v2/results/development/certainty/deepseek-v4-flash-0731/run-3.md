{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "다음 단계로 넘길 대상이 정산 결과의 어떤 부분이며, 다리라는 비유가 실제로 어떤 전달 방식(API, 메시지, 파일 등)을 뜻하는지",
      "suggested_revision": "정산 결과를 다음 단계로 전달하는 인터페이스를 추가합니다.",
      "verification_question": "정산 결과를 다음 단계로 전달하는 구체적인 방식(API, 메시지, 파일 등)은 무엇입니까?"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "예외를 받아낸다는 동작이 실제로 무엇을 의미하는지(예외를 잡아서 처리, 별도 저장, 무시 등)와 완충지대가 어떤 구조인지",
      "suggested_revision": "예외를 처리하는 별도 구간을 둡니다.",
      "verification_question": "예외를 받아낸다는 동작이 예외를 잡아서 처리하는 것인지, 별도로 저장하는 것인지, 무시하는 것인지 명확히 알려주십시오."
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "통계 값을 화면으로 끌어올린다는 동작이 실제로 무엇인지(API 응답에 포함, 화면에 표시, 데이터 전송 등)와 손잡이가 어떤 메커니즘인지",
      "suggested_revision": "통계 값을 화면에 표시할 수 있도록 조회 기능을 추가합니다.",
      "verification_question": "통계 값을 화면으로 전달하는 구체적인 방법(API 응답, 화면 표시, 데이터 전송 등)은 무엇입니까?"
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
      "reader_must_infer": "월말 마감 이후 전표 수정이 불가하다는 규칙의 주체와 예외, 오류 전표를 취소 후 재작성한다는 절차의 주체",
      "suggested_revision": "월말 마감 이후에는 전표를 수정할 수 없습니다. 오류 전표는 취소한 후 재작성해야 합니다.",
      "verification_question": "월말 마감 이후 전표 수정이 불가한 주체(사용자, 시스템)와 오류 전표를 취소 후 재작성하는 주체가 명확히 정의되어 있습니까?"
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
