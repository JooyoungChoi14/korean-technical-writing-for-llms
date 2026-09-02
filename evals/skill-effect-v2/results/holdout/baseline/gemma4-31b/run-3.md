```json
{
  "cases": [
    {
      "id": "H-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "관문이라는 비유가 실제 어떤 기술적 동작(API 게이트웨이 도입, 메시지 큐 전송, 특정 모듈 추가 등)을 의미하는지",
      "suggested_revision": "감사 로그를 외부 분석기로 전송하기 위한 전송 모듈(또는 게이트웨이)을 구현합니다.",
      "verification_question": "관문이 구체적으로 어떤 컴포넌트나 인터페이스를 의미합니까?"
    },
    {
      "id": "H-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "쿠션이라는 비유가 구체적으로 어떤 메커니즘(버퍼 메모리, 안전 재고 설정, 대기 큐 등)을 통해 부족분을 해결하는지",
      "suggested_revision": "재고 부족 시 서비스 중단을 막기 위해 안전 재고(또는 버퍼)를 설정합니다.",
      "verification_question": "쿠션이 의미하는 구체적인 재고 관리 방식이나 기술적 장치는 무엇입니까?"
    },
    {
      "id": "H-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "소켓을 연다는 비유가 어떤 동작(API 엔드포인트 생성, UI 컴포넌트 인터페이스 정의, 데이터 바인딩 설정 등)을 의미하는지",
      "suggested_revision": "모델 판정값을 업무 화면에 표시할 수 있도록 데이터 인터페이스(또는 API)를 제공합니다.",
      "verification_question": "소켓을 연다는 것이 API를 추가하는 것인지, UI의 특정 영역을 정의하는 것인지 확인이 필요합니다."
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
      "reader_must_infer": "적용하는 대상(권한, 접근 제어 등)과 '순으로 적용'한다는 것이 우선순위인지 평가 순서인지",
      "suggested_revision": "문서 접근 권한은 현장 관리자(공개), 본사 보안(비공개), 문서 소유자(공개), 기본(비공개) 순으로 확인하며, 설정 중 '비공개'가 하나라도 있으면 최종적으로 비공개 처리합니다.",
      "verification_question": "적용 대상이 '문서 접근 권한'이 맞으며, 비공개 우선 원칙이 모든 조건에 대해 적용되는 것이 맞습니까?"
    },
    {
      "id": "H-C02",
      "decision": "구체화 필요",
      "reader_must_infer": "적용 대상(출고 상태, 승인 프로세스 등)과 '보류를 승인보다 우선한다'는 구체적인 판정 로직",
      "suggested_revision": "출고 상태는 긴급 출고 승인, 품질 보류, 영업 승인, 기본 거절 순으로 판정하며, 승인 상태보다 보류 상태를 우선하여 적용합니다.",
      "verification_question": "판정 대상이 '출고 상태'가 맞으며, 보류와 승인이 동시에 존재할 때 보류로 처리한다는 의미입니까?"
    },
    {
      "id": "H-C03",
      "decision": "구체화 필요",
      "reader_must_infer": "판정 대상(참여 자격, 동의 여부 등)과 '제외를 동의보다 우선'하는 구체적인 결과",
      "suggested_revision": "연구 참여 자격은 환자 직접 동의, 연구 제외 등록, 기관 동의, 기본 제외 순으로 판정하며, 제외 조건이 충족되면 동의 여부와 상관없이 최종 '제외'로 처리합니다.",
      "verification_question": "판정 대상이 '연구 참여 자격'이 맞으며, 제외 조건이 동의 조건보다 우선순위가 높다는 의미입니까?"
    },
    {
      "id": "H-N01",
      "decision": "구체화 필요",
      "reader_must_infer": "주체와 서술어가 생략된 명사 나열로 인해, 이것이 작업 순서인지 결과인지",
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
