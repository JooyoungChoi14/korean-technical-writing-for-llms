```json
{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "“다리”가 구체적으로 어떤 구성 요소인지(메시지 큐, 배치 파이프라인, API 호출 등)",
      "suggested_revision": "정산 결과를 다음 처리 단계로 전달하는 구성 요소가 필요합니다.",
      "verification_question": "“다리”가 가리키는 구성 요소는 무엇입니까? (메시지 큐, 파일 전달, API 호출 등)"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "“완충지대”가 구체적으로 어떤 예외 처리 구조인지(재시도 큐, 데드 레터 큐, 예외 로그 저장 등)",
      "suggested_revision": "예외를 수집하여 보관하는 큐를 둡니다.",
      "verification_question": "“완충지대”는 어떤 예외 처리 방식을 가리킵니까? (재시도 큐, 데드 레터 큐, 예외 로그 저장 등)"
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "“손잡이”가 구체적으로 어떤 API나 속성인지(API 엔드포인트, 상태 속성, 데이터 바인딩 등)",
      "suggested_revision": "통계 값을 화면에 전달하는 API 엔드포인트를 추가합니다.",
      "verification_question": "“손잡이”는 어떤 구성 요소를 가리킵니까? (API 엔드포인트, 상태 속성, 데이터 바인딩 등)"
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
      "reader_must_infer": "오류 전표의 취소 후 재작성을 수행하는 주체가 사용자인지 시스템인지",
      "suggested_revision": "월말 마감이 완료된 이후에는 전표를 수정할 수 없습니다. 오류 전표는 취소한 뒤 다시 작성해야 합니다.",
      "verification_question": "오류 전표의 취소 및 재작성은 사용자가 수동으로 수행해야 합니까, 아니면 시스템이 자동으로 처리합니까?"
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
```
