```json
{
  "cases": [
    {
      "id": "H-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "관문이라는 비유가 구체적으로 어떤 기술적 구성 요소(API Gateway, Message Queue, Interface 등)를 의미하는지",
      "suggested_revision": "감사 로그를 외부 분석기로 전송하기 위한 인터페이스를 구축합니다.",
      "verification_question": null
    },
    {
      "id": "H-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "쿠션이라는 비유가 구체적으로 어떤 동작(버퍼링, 임시 저장소 확보, 재고 여유분 설정 등)을 의미하는지",
      "suggested_revision": "재고 부족 시 서비스 중단을 방지하기 위해 임시 버퍼를 확보해야 합니다.",
      "verification_question": null
    },
    {
      "id": "H-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "소켓을 연다는 비유가 구체적으로 어떤 동작(API 엔드포인트 추가, 데이터 바인딩 설정, UI 컴포넌트 배치 등)을 의미하는지",
      "suggested_revision": "모델 판정값을 업무 화면에 표시할 수 있도록 데이터 인터페이스를 추가합니다.",
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
      "reader_must_infer": "적용 순서와 우선순위의 관계(순차적으로 확인하다가 먼저 발견된 것을 적용하는지, 모든 조건을 확인한 후 특정 값에 가중치를 두는지)",
      "suggested_revision": "권한은 현장 관리자, 본사 보안, 문서 소유자, 기본 설정 순으로 확인하며, 조건 중 하나라도 '비공개'가 있으면 최종적으로 비공개 처리합니다.",
      "verification_question": null
    },
    {
      "id": "H-C02",
      "decision": "구체화 필요",
      "reader_must_infer": "적용 순서와 우선순위의 관계 및 '보류'가 '승인'보다 우선한다는 구체적인 결과",
      "suggested_revision": "승인 여부는 긴급 출고 승인, 품질 보류, 영업 승인, 기본 거절 순으로 확인하며, 승인과 보류 조건이 동시에 충족되면 '보류'로 판정합니다.",
      "verification_question": null
    },
    {
      "id": "H-C03",
      "decision": "구체화 필요",
      "reader_must_infer": "판정 순서와 우선순위의 관계 및 '제외'가 '동의'보다 우선한다는 구체적인 결과",
      "suggested_revision": "참여 여부는 환자 직접 동의, 연구 제외 등록, 기관 동의, 기본 제외 순으로 확인하며, 동의와 제외 조건이 동시에 충족되면 '제외'로 판정합니다.",
      "verification_question": null
    },
    {
      "id": "H-N01",
      "decision": "구체화 필요",
      "reader_must_infer": "주체와 서술어가 생략된 명사 나열로 인해, 이것이 작업 순서인지 결과인지 혹은 요구사항인지",
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
