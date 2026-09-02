{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "다리라는 비유가 실제로 무엇을 의미하는지(어떤 데이터 구조, API, 변환 단계 등)를 추측해야 함",
      "suggested_revision": "정산 결과를 다음 단계로 전달하는 중간 저장소(또는 API)를 추가합니다.",
      "verification_question": "정산 결과를 다음 단계로 넘기는 구체적인 방법은 무엇인가요? (예: 테이블, 메시지 큐, API 응답)"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "완충지대가 예외를 받아내는 구체적인 동작(예외 처리 로직, 재시도, 로깅 등)을 추측해야 함",
      "suggested_revision": "예외를 처리하는 별도 로직(예: 재시도 및 로깅)을 둡니다.",
      "verification_question": "예외를 받아낸다는 구체적인 처리는 무엇인가요? (예: 재시도, 큐 적재, 오류 로그 기록)"
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "손잡이가 실제로 무엇을 의미하는지(API 엔드포인트, UI 컴포넌트, 데이터 바인딩 등)를 추측해야 함",
      "suggested_revision": "통계 값을 화면에 표시할 수 있도록 조회 API(또는 데이터 바인딩)를 추가합니다.",
      "verification_question": "통계 값을 화면으로 가져오는 구체적인 방법은 무엇인가요? (예: REST API, GraphQL, 서버 렌더링)"
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
      "reader_must_infer": "주어가 생략되어 누가 전표를 수정/취소/재작성하는지, 그리고 '불가'의 주체(시스템 제한인지 정책인지)를 추측해야 함",
      "suggested_revision": "월말 마감 이후에는 전표를 수정할 수 없으며, 오류 전표는 취소 후 재작성해야 합니다.",
      "verification_question": "전표 수정을 막는 주체는 시스템(기능 제한)인가요, 아니면 업무 정책인가요?"
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
