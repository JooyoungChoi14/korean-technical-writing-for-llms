```json
{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "정산 결과를 다음 단계로 전달할 구체적인 수단(API, 큐, 파이프라인 등)이 무엇인지",
      "suggested_revision": "정산 결과를 다음 단계로 전달하는 컴포넌트(예: 메시지 큐 또는 API)가 필요합니다.",
      "verification_question": "정산 결과를 다음 단계로 넘기는 실제 구성 요소는 무엇입니까?"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "예외를 수신·처리하는 구체적인 구성 요소(예외 처리 모듈, 재시도 큐, 데드 레터 큐 등)가 무엇인지",
      "suggested_revision": "예외를 수신하여 처리할 예외 처리 모듈(또는 재시도 큐)를 둡니다.",
      "verification_question": "예외를 받아내는 구성 요소와 예외 처리 방식은 무엇입니까?"
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "통계 값을 화면에 표시하기 위해 추가하는 구체적인 인터페이스(조회 API, 데이터 바인딩 등)가 무엇인지",
      "suggested_revision": "통계 값을 화면에 표시할 수 있도록 조회 API(또는 데이터 바인딩)를 추가합니다.",
      "verification_question": "통계 값을 화면으로 가져오기 위해 추가하는 인터페이스의 종류는 무엇입니까?"
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
      "reader_must_infer": "전표 수정을 금지하는 주체와 절차, 오류 전표를 취소 후 재작성하는 주체와 절차",
      "suggested_revision": "월말 마감이 완료된 이후에는 전표를 수정할 수 없으며, 오류가 발생한 전표는 취소한 뒤 다시 작성해야 합니다.",
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
```
