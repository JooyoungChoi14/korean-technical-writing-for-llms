```json
{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "‘다리’가 구체적으로 어떤 기술적 수단(예: API, 큐, 파이프라인)인지",
      "suggested_revision": "정산 결과를 다음 단계로 전달하는 API(또는 큐)를 추가합니다.",
      "verification_question": "‘다리’가 가리키는 실제 구현 요소는 무엇입니까?"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "‘완충지대’가 구체적으로 어떤 예외 처리 기제(예: 예외 처리 모듈, 데드 레터 큐)인지",
      "suggested_revision": "예외를 수집하여 처리하는 예외 처리 모듈(또는 큐)을 둡니다.",
      "verification_question": "‘완충지대’가 가리키는 실제 예외 처리 구성 요소는 무엇입니까?"
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "‘손잡이’가 구체적으로 어떤 인터페이스(예: API 엔드포인트, 상태 속성)인지",
      "suggested_revision": "화면이 통계 값을 읽을 수 있도록 API 엔드포인트를 추가합니다.",
      "verification_question": "‘손잡이’가 가리키는 실제 인터페이스는 무엇입니까?"
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
      "reader_must_infer": "서술어가 생략되어 있어 동작의 확정성이 부족함",
      "suggested_revision": "월말 마감 이후에는 전표를 수정할 수 없으며, 오류 전표는 취소한 후 다시 작성합니다.",
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
