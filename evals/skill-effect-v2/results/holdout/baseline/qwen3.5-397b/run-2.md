{
  "cases": [
    {
      "id": "H-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "\"관문\"의 실제 기술 구성 요소",
      "suggested_revision": "감사 로그를 외부 분석기로 전송하는 중계 구성 요소를 둡니다.",
      "verification_question": "\"관문\"으로 지칭하는 실제 기술 구성 요소 (API Gateway, Log Shipper 등) 는 무엇입니까?"
    },
    {
      "id": "H-A02",
      "decision": "의미 확인 필요",
      "reader_must_infer": "\"쿠션\"이 의미하는 구체적 방식",
      "suggested_revision": "재고 부족분을 보완할 안전 재고 (Safety Stock) 가 필요합니다.",
      "verification_question": "\"쿠션\"이 안전 재고를 의미하는지, 아니면 별도의 버퍼 논리를 의미하는지 확인이 필요합니다."
    },
    {
      "id": "H-A03",
      "decision": "의미 확인 필요",
      "reader_must_infer": "\"소켓\"이 의미하는 인터페이스 종류",
      "suggested_revision": "모델 판정값을 업무 화면에 표시할 API 엔드포인트를 추가합니다.",
      "verification_question": "\"소켓\"이 API 인터페이스를 의미하는지, UI 컴포넌트 슬롯을 의미하는지 확인이 필요합니다."
    },
    {
      "id": "H-P01",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "H-P02",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "H-P03",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "H-C01",
      "decision": "구체화 필요",
      "reader_must_infer": "우선순위 충돌 시 해결 기준",
      "suggested_revision": "접근 권한은 현장 관리자 공개, 본사 보안 비공개, 문서 소유자 공개, 기본 비공개 순으로 평가하며, 충돌 시 비공개 설정이 우선합니다.",
      "verification_question": "\"비공개를 우선합니다\"가 모든 공개 설정보다 우선하는지 확인이 필요합니다."
    },
    {
      "id": "H-C02",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "H-C03",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "H-N01",
      "decision": "구체화 필요",
      "reader_must_infer": "주체 및 실행 시점",
      "suggested_revision": "결측치를 대치한 후 회귀 모델을 재학습하며, 기존 계수는 폐기합니다.",
      "verification_question": "이 작업이 자동 프로세스인지 수동 명령인지 확인이 필요합니다."
    },
    {
      "id": "H-P04",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "H-P05",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    }
  ]
}
