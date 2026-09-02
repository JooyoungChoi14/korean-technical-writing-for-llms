{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "'다리'라는 비유가 구체적으로 어떤 기술 구성 요소 (API, 큐, 파일 전송 등) 를指하는지",
      "suggested_revision": "정산 결과를 다음 단계로 전달할 연결 기능이 필요합니다.",
      "verification_question": null
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "'완충지대'가 예외를 잡는 코드 구문인지, 대기 큐인지, 재시도 로직인지",
      "suggested_revision": "예외를 처리할 오류 핸들링 로직을 둡니다.",
      "verification_question": null
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "'손잡이'가 UI 버튼인지, API 엔드포인트인지, getter 메서드인지",
      "suggested_revision": "화면이 통계 값을 조회할 수 있는 인터페이스를 추가합니다.",
      "verification_question": null
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
      "reader_must_infer": "'기본 가격'이 적용 순서의 마지막 단계인지, 아니면 계산의 기준점인지",
      "suggested_revision": null,
      "verification_question": "기본 가격이 할인 적용 순서의 마지막 단계로 명시된 것이 맞습니까? 아니면 계산의 기준점입니까?"
    },
    {
      "id": "DEV-C02",
      "decision": "구체화 필요",
      "reader_must_infer": "명사 나열로 된 판정 순서의 실제 제어 흐름 (if-else 여부)",
      "suggested_revision": "수동 승인, 자동 보류, 부서 승인 순으로 판정하며 해당되지 않으면 기본 거절합니다. 보류는 승인보다 우선합니다.",
      "verification_question": null
    },
    {
      "id": "DEV-C03",
      "decision": "구체화 필요",
      "reader_must_infer": "명사 나열로 된 적용 순서의 실제 제어 흐름과 기본값의 의미",
      "suggested_revision": "사용자 알림 허용, 조직 알림 차단, 채널 허용 순으로 적용하며 해당되지 않으면 기본 차단합니다. 차단 설정은 항상 우선합니다.",
      "verification_question": null
    },
    {
      "id": "DEV-N01",
      "decision": "구체화 필요",
      "reader_must_infer": "주체와 서술어가 생략되어 누가 수정할 수 없는지, 오류 전표 처리 주체가 누구인지",
      "suggested_revision": "월말 마감 이후에는 전표를 수정할 수 없습니다. 오류가 발생한 전표는 취소한 후 재작성해야 합니다.",
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
