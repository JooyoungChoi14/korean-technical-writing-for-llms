```json
{
  "cases": [
    {
      "id": "H-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "관문이라는 비유가 구체적으로 어떤 인터페이스나 모듈(예: API Gateway, Message Queue, 전송 모듈)을 의미하는지",
      "suggested_revision": "감사 로그를 외부 분석기로 전송하는 전송 모듈을 구현합니다.",
      "verification_question": null
    },
    {
      "id": "H-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "쿠션이라는 비유가 구체적으로 어떤 기술적 장치(예: 버퍼, 큐, 안전 재고 설정)를 의미하는지",
      "suggested_revision": "재고 부족 시 서비스 중단을 막기 위해 버퍼 재고를 설정합니다.",
      "verification_question": null
    },
    {
      "id": "H-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "소켓을 연다는 비유가 구체적으로 어떤 동작(예: API 엔드포인트 추가, UI 컴포넌트 인터페이스 정의)을 의미하는지",
      "suggested_revision": "모델 판정값을 업무 화면에 표시할 수 있도록 API 엔드포인트를 추가합니다.",
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
      "reader_must_infer": "적용 순서와 우선순위의 관계(순차적으로 확인하다가 먼저 발견된 것을 적용하는지, 모든 조건을 확인한 후 비공개 여부를 최종 결정하는지)",
      "suggested_revision": "현장 관리자, 본사 보안, 문서 소유자, 기본 설정 순으로 권한을 확인하며, 하나라도 '비공개' 조건에 해당하면 최종적으로 비공개 처리합니다.",
      "verification_question": null
    },
    {
      "id": "H-C02",
      "decision": "구체화 필요",
      "reader_must_infer": "적용 순서와 우선순위의 관계 및 '보류'가 '승인'보다 우선한다는 구체적인 결과",
      "suggested_revision": "긴급 출고 승인, 품질 보류, 영업 승인, 기본 거절 순으로 상태를 확인하며, 승인 조건과 보류 조건이 동시에 충족되면 '보류'로 판정합니다.",
      "verification_question": null
    },
    {
      "id": "H-C03",
      "decision": "구체화 필요",
      "reader_must_infer": "판정 순서와 우선순위의 관계 및 '제외'가 '동의'보다 우선한다는 구체적인 결과",
      "suggested_revision": "환자 직접 동의, 연구 제외 등록, 기관 동의, 기본 제외 순으로 판정하며, 동의 조건과 제외 조건이 동시에 충족되면 '제외'로 판정합니다.",
      "verification_question": null
    },
    {
      "id": "H-N01",
      "decision": "구체화 필요",
      "reader_must_infer": "주체와 서술어가 생략된 명사 나열로 인해, 이것이 작업 지시인지 시스템 동작 정의인지",
      "suggested_revision": "결측치를 대치한 후 회귀 모델을 재학습시키고, 기존의 계수 값은 폐기합니다.",
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
