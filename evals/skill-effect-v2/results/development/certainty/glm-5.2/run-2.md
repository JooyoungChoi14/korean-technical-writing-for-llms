```json
{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "‘다리’가 큐, 파이프라인 단계, API 엔드포인트, 데이터 전송 컴포넌트 중 무엇인지",
      "suggested_revision": "정산 결과를 다음 처리 단계로 전달하는 컴포넌트가 필요합니다.",
      "verification_question": "‘다리’는 실제로 어떤 구현 요소(큐, 파이프라인, API 등)를 가리킵니까?"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "‘완충지대’가 에러 큐, 예외 처리 모듈, 데드 레터 큐, 재시도 버퍼 중 무엇인지",
      "suggested_revision": "예외를 수집하여 처리할 에러 큐를 둡니다.",
      "verification_question": "‘완충지대’는 실제로 어떤 구현 요소(에러 큐, 예외 처리 모듈 등)를 가리킵니까?"
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "‘손잡이’가 API 엔드포인트, 조회 함수, 데이터 바인딩, UI 컴포넌트 중 무엇인지",
      "suggested_revision": "통계 값을 화면에 표시할 조회 API를 추가합니다.",
      "verification_question": "‘손잡이’는 실제로 어떤 구현 요소(API 엔드포인트, 조회 함수 등)를 가리킵니까?"
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
      "reader_must_infer": "전표 수정을 막는 주체(시스템, 권한 정책)와 취소·재작성을 수행하는 주체(사용자, 시스템)가 생략됨",
      "suggested_revision": "월말 마감 이후에는 시스템이 전표 수정을 허용하지 않으며, 오류 전표는 취소 후 재작성해야 합니다.",
      "verification_question": "전표 수정 불가는 시스템이 자동으로 차단하는 것인지, 권한 정책으로 통제하는 것인지?"
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
