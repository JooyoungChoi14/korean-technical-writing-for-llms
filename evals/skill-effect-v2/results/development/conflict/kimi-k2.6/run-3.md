```json
{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "'다리'가 가리키는 실제 구성 요소(인터페이스, 데이터 전달 로직, 연동 모듈 등)와 '넘긴다'의 구체적인 동작",
      "suggested_revision": "정산 결과를 다음 단계로 전달하는 연동 로직을 추가합니다.",
      "verification_question": "'다음 단계'는 어떤 시스템 또는 모듈을 가리키며, 전달 방식은 무엇인가?"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "'완충지대'가 가리키는 실제 메커니즘(예외 핸들러, 폴백 로직, 버퍼 등)과 예외를 처리하는 주체",
      "suggested_revision": "예외를 처리할 핸들러를 추가합니다.",
      "verification_question": "예외를 받아낸 후 어떤 동작(로깅, 폴백, 재시도 등)을 수행하며, 처리 주체는 무엇인가?"
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "'손잡이'가 가리키는 실제 구성 요소(API 엔드포인트, 조회 메서드, 화면 속성 등)",
      "suggested_revision": "통계 값을 화면에 노출할 조회 API를 추가합니다.",
      "verification_question": "화면이 통계 값을 가져오는 방식은 API 호출, 메서드 호출, 속성 노출 중 무엇인가?"
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
      "reader_must_infer": "'전표 수정 불가'와 '재작성'의 주체(사용자, 시스템, 담당자 등)와 '불가'의 실제 효과(시스템 차단, 정책 금지 등)",
      "suggested_revision": "월말 마감 이후에는 전표를 수정할 수 없으며, 오류가 발생한 전표는 취소한 뒤 재작성해야 합니다.",
      "verification_question": "전표 수정 및 재작성의 주체는 누구이며, 수정 불가는 시스템 차단인가, 정책상 금지인가?"
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
