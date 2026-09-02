```json
{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "“다리”가 구체적으로 어떤 컴포넌트·API·데이터 전달 수단인지",
      "suggested_revision": "정산 결과를 다음 단계로 전달하는 인터페이스(또는 큐·필드)를 추가합니다.",
      "verification_question": "“다리”가 가리키는 구체적인 구성 요소(API, 메시지 큐, 데이터 필드 등)는 무엇입니까?"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "“완충지대”가 실제로 어떤 예외 처리 구조(재시도, 폴백, 데드레터 큐 등)인지",
      "suggested_revision": "예외를 처리할 fallback 핸들러(또는 재시도 큐)를 둡니다.",
      "verification_question": "“완충지대”가 가리키는 구체적인 예외 처리 방식은 무엇입니까?"
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "“손잡이”가 어떤 API·속성·쿼리인지, “끌어올리다”가 어떤 데이터 전달 동작인지",
      "suggested_revision": "통계 값을 화면에 표시할 수 있도록 조회 API(또는 상태 속성)를 추가합니다.",
      "verification_question": "“손잡이”가 가리키는 구체적인 구현(API 엔드포인트, 상태 속성, 쿼리 등)은 무엇입니까?"
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
      "reader_must_infer": "수정 불가의 제약을 적용하는 주체와 방식, 취소 후 재작성의 수행 주체",
      "suggested_revision": "월말 마감 이후에는 전표를 수정할 수 없으며, 오류 전표는 취소한 뒤 다시 작성해야 합니다.",
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
