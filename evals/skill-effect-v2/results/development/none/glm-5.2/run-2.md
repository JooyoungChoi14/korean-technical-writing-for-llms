```json
{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "'다리'가 데이터 전달 인터페이스, 큐, 파일 연계 등 구체적으로 무엇인지 추론해야 함",
      "suggested_revision": "정산 결과를 다음 단계로 전달하기 위한 데이터 연계 큐를 구성합니다.",
      "verification_question": "'다리'는 데이터 전달용 큐, 파일, API 중 어떤 수단을 의미합니까?"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "'완충지대'가 예외 처리 로직, 데드레터큐, 재시도 버퍼 등 구체적으로 무엇인지 추론해야 함",
      "suggested_revision": "예외를 수집하는 데드레터큐를 배치 처리 단계 사이에 둡니다.",
      "verification_question": "'완충지대'는 예외를 일시 보관하는 큐인지, 예외 처리 로직인지 명확히 해 주세요."
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "'손잡이'가 API 엔드포인트, 데이터 조회 함수, UI 컴포넌트 중 무엇인지 추론해야 함",
      "suggested_revision": "통계 값을 화면에 조회하기 위한 API 엔드포인트를 추가합니다.",
      "verification_question": "'손잡이'는 API 엔드포인트, 프론트엔드 조회 함수, UI 버튼 중 어떤 것입니까?"
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
      "reader_must_infer": "나열된 순서가 적용 우선순위인지 평가 순서인지, '제외 조건 우선'이 나열 순서와 어떻게 관련되는지 추론해야 함",
      "suggested_revision": "할인 적용 전 제외 조건을 먼저 평가합니다. 제외 대상이 아니면 개별 상품 할인, 회원 등급 할인, 기본 가격 순으로 적용합니다.",
      "verification_question": "나열된 순서는 적용 우선순위입니까, 아니면 평가 순서입니까? '제외 조건 우선'은 나열 순서와 별개의 규칙입니까?"
    },
    {
      "id": "DEV-C02",
      "decision": "의미 확인 필요",
      "reader_must_infer": "나열된 순서가 판정 우선순위인지 평가 순서인지, '보류 우선'이 나열 순서와 어떻게 관련되는지 추론해야 함",
      "suggested_revision": "자동 보류 조건을 먼저 평가하고, 보류 대상이 아니면 수동 승인, 부서 승인, 기본 거절 순으로 판정합니다.",
      "verification_question": "나열된 순서는 판정 우선순위입니까, 아니면 평가 순서입니까? '보류 우선'은 나열 순서와 별개의 규칙입니까?"
    },
    {
      "id": "DEV-C03",
      "decision": "의미 확인 필요",
      "reader_must_infer": "나열된 순서가 적용 우선순위인지 평가 순서인지, '차단 항상 우선'이 나열 순서와 어떻게 관련되는지 추론해야 함",
      "suggested_revision": "차단 조건(조직 알림 차단, 기본 차단)을 먼저 평가하고, 차단되지 않으면 사용자 알림 허용, 채널 허용 순으로 적용합니다.",
      "verification_question": "나열된 순서는 적용 우선순위입니까, 아니면 평가 순서입니까? '차단 항상 우선'은 나열 순서와 별개의 규칙입니까?"
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
```
