```json
{
  "cases": [
    {
      "id": "H-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "관문이라는 비유가 구체적으로 어떤 기술적 동작(API 엔드포인트 생성, 메시지 큐 도입, 프록시 설정 등)을 의미하는지",
      "suggested_revision": "감사 로그를 외부 분석기로 전송하기 위한 인터페이스(또는 API 엔드포인트)를 구축합니다.",
      "verification_question": null
    },
    {
      "id": "H-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "쿠션이라는 비유가 구체적으로 어떤 메커니즘(버퍼 큐 도입, 안전 재고 설정, 임시 저장소 확보 등)을 의미하는지",
      "suggested_revision": "재고 부족 시 서비스 중단을 막기 위해 버퍼(또는 안전 재고)를 확보합니다.",
      "verification_question": null
    },
    {
      "id": "H-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "소켓을 연다는 비유가 구체적으로 어떤 동작(API 필드 추가, UI 컴포넌트 배치, 데이터 바인딩 설정 등)을 의미하는지",
      "suggested_revision": "모델 판정값을 업무 화면에 표시할 수 있도록 데이터 필드(또는 API 속성)를 추가합니다.",
      "verification_question": null
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
      "reader_must_infer": "적용 순서와 우선순위의 관계(순차적으로 확인하여 먼저 매칭되는 것을 쓰는지, 모든 조건을 확인한 후 비공개 설정이 하나라도 있으면 비공개로 처리하는지)",
      "suggested_revision": "현장 관리자, 본사 보안, 문서 소유자, 기본 설정 순으로 권한을 확인하며, 설정 중 '비공개'가 하나라도 포함되면 최종적으로 비공개 처리합니다.",
      "verification_question": "권한 판정 시 '우선한다'는 의미가 '먼저 발견된 규칙을 적용한다'는 뜻인지, '상충하는 규칙 중 특정 값에 가중치를 둔다'는 뜻인지 확인이 필요합니다."
    },
    {
      "id": "H-C02",
      "decision": "구체화 필요",
      "reader_must_infer": "보류가 승인보다 우선한다는 구체적인 판정 로직(보류 상태가 있으면 승인 여부와 상관없이 보류로 처리하는지 등)",
      "suggested_revision": "긴급 출고 승인, 품질 보류, 영업 승인, 기본 거절 순으로 판정하며, '보류' 상태가 확인되면 '승인' 상태보다 우선하여 보류로 처리합니다.",
      "verification_question": "보류와 승인이 동시에 존재할 때의 최종 상태 결정 로직이 무엇인지 확인이 필요합니다."
    },
    {
      "id": "H-C03",
      "decision": "구체화 필요",
      "reader_must_infer": "제외가 동의보다 우선한다는 구체적인 판정 로직",
      "suggested_revision": "환자 직접 동의, 연구 제외 등록, 기관 동의, 기본 제외 순으로 판정하며, '제외' 조건이 하나라도 충족되면 '동의' 여부와 상관없이 최종 제외로 처리합니다.",
      "verification_question": "제외와 동의가 충돌할 때의 최종 판정 기준이 무엇인지 확인이 필요합니다."
    },
    {
      "id": "H-N01",
      "decision": "구체화 필요",
      "reader_must_infer": "명사 나열로 인해 주체와 동작이 생략됨 (결측치를 대치한 후 모델을 재학습시키고 기존 계수를 삭제한다는 의미인지)",
      "suggested_revision": "결측치를 대치한 후 회귀 모델을 재학습시키며, 기존의 계수 값은 폐기합니다.",
      "verification_question": null
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
```
