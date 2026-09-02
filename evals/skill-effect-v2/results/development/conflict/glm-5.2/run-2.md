```json
{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "정산 결과를 다음 단계로 전달하는 실제 메커니즘(메시지 큐, API 호출, 파이프라인 등)이 무엇인지",
      "suggested_revision": "정산 결과를 다음 단계로 전달하는 연결 수단(예: 메시지 큐 또는 API 호출)을 추가합니다.",
      "verification_question": "다리가 가리키는 실제 구성 요소는 무엇입니까?(메시지 큐, API 엔드포인트, 배치 파이프라인 등)"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "완충지대가 실제로 어떤 메커니즘(예외 핸들러, 재시도 큐, 데드 레터 큐, 폴백 로직 등)인지",
      "suggested_revision": "예외를 수신하여 처리할 예외 핸들러(또는 재시도 큐)를 둡니다.",
      "verification_question": "완충지대가 실제로 어떤 구성 요소입니까?(예외 핸들러, 재시도 큐, 데드 레터 큐, 폴백 로직 등)"
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "손잡이가 실제로 어떤 API나 속성인지, 끌어올린다는 것이 어떤 동작(조회, 바인딩, 노출 등)인지",
      "suggested_revision": "화면이 통계 값을 읽을 수 있도록 조회 API(또는 상태 속성)를 추가합니다.",
      "verification_question": "추가할 손잡이가 실제로 어떤 인터페이스입니까?(API 엔드포인트, 상태 속성, 데이터 바인딩 등)"
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
      "reader_must_infer": "전표를 수정하거나 취소 후 재작성하는 주체가 누구인지, 월말 마감의 정확한 조건이 무엇인지",
      "suggested_revision": "월말 마감이 완료된 이후에는 전표를 수정할 수 없으며, 오류 전표는 취소한 뒤 새로 작성해야 합니다.",
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
