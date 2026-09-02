{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "다음 단계로 넘기는 구체적인 방법(함수 호출, 메시지 큐, 테이블 저장 등)",
      "suggested_revision": "정산 결과를 다음 단계로 전달하는 인터페이스를 추가합니다.",
      "verification_question": "다음 단계로 전달하는 구체적인 방법(함수 호출, 메시지 큐, 테이블 저장 등)은 무엇입니까?"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "예외를 처리하는 위치와 방식(try-catch, 오류 변환 계층 등)",
      "suggested_revision": "예외를 잡아 처리하는 로직을 추가합니다.",
      "verification_question": "예외를 처리하는 위치와 방식(try-catch, 오류 변환 계층 등)은 무엇입니까?"
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "화면이 통계 값을 가져오는 경로(API 엔드포인트, 응답 필드 등)",
      "suggested_revision": "통계 값을 화면에 표시하기 위한 조회 기능을 추가합니다.",
      "verification_question": "화면이 통계 값을 가져오는 방법(API 엔드포인트, 응답 필드 등)은 무엇입니까?"
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
      "reader_must_infer": "제외 조건의 범위와 '할인보다 우선'이 적용 순서에 반영되는 방식",
      "suggested_revision": null,
      "verification_question": "제외 조건이 캠페인 제외만을 의미하는지, 그리고 '할인보다 우선'이 적용 순서상 어느 단계를 뜻하는지 확인이 필요합니다."
    },
    {
      "id": "DEV-C02",
      "decision": "의미 확인 필요",
      "reader_must_infer": "보류가 승인보다 우선할 때 확인 시점(승인 전인지 후인지)",
      "suggested_revision": null,
      "verification_question": "보류 조건이 수동 승인보다 먼저 확인되어야 하는지, 아니면 승인 후에도 보류가 우선하는지 확인이 필요합니다."
    },
    {
      "id": "DEV-C03",
      "decision": "의미 확인 필요",
      "reader_must_infer": "차단 우선이 조직 차단만 해당하는지 기본 차단도 포함하는지",
      "suggested_revision": null,
      "verification_question": "조직 알림 차단이 사용자 알림 허용보다 항상 우선하는지, 기본 차단도 허용보다 우선하는지 확인이 필요합니다."
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
