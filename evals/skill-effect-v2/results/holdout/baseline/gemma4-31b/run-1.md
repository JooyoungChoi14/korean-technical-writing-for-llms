```json
{
  "cases": [
    {
      "id": "H-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "관문이라는 비유가 구체적으로 어떤 기술적 구성 요소(API Gateway, Message Queue, Proxy 등)를 의미하는지, 데이터 전송 방식은 무엇인지",
      "suggested_revision": "감사 로그를 외부 분석기로 전송하기 위한 인터페이스(또는 전송 모듈)를 구현합니다.",
      "verification_question": "관문이 구체적으로 어떤 컴포넌트나 아키텍처 패턴을 의미합니까?"
    },
    {
      "id": "H-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "쿠션이라는 비유가 구체적으로 어떤 동작(버퍼링, 재고 여유분 확보, 대기열 생성 등)을 통해 재고 부족을 해결한다는 것인지",
      "suggested_revision": "재고 부족 시 서비스 중단을 막기 위해 일정량의 안전 재고를 확보하거나 요청 대기열을 둡니다.",
      "verification_question": "재고 부족을 흡수하기 위해 기술적으로 어떤 장치(버퍼, 안전 재고 등)를 도입하려는 것입니까?"
    },
    {
      "id": "H-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "소켓을 연다는 비유가 구체적으로 어떤 동작(API 엔드포인트 추가, UI 컴포넌트 슬롯 정의, 데이터 바인딩 설정 등)인지",
      "suggested_revision": "모델 판정값을 업무 화면에 표시할 수 있도록 데이터 인터페이스(또는 API 엔드포인트)를 제공합니다.",
      "verification_question": "소켓을 연다는 것이 API를 추가하는 것입니까, 아니면 UI의 특정 영역을 정의하는 것입니까?"
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
      "reader_must_infer": "적용 대상(권한, 접근 제어 등)이 무엇인지, '순으로 적용'한다는 것이 우선순위인지 평가 순서인지",
      "suggested_revision": "접근 권한은 현장 관리자(공개), 본사 보안(비공개), 문서 소유자(공개), 기본(비공개) 순으로 확인하며, 하나라도 비공개 설정이 있으면 최종적으로 비공개 처리합니다.",
      "verification_question": "적용 대상이 '문서 접근 권한'이 맞습니까?"
    },
    {
      "id": "H-C02",
      "decision": "구체화 필요",
      "reader_must_infer": "적용 대상(출고 상태, 승인 여부 등)이 무엇인지, '보류를 승인보다 우선'한다는 것이 최종 상태 결정 로직인지",
      "suggested_revision": "출고 상태는 긴급 출고 승인, 품질 보류, 영업 승인, 기본 거절 순으로 판정하며, 승인 상태보다 보류 상태를 우선하여 최종 상태를 결정합니다.",
      "verification_question": "적용 대상이 '출고 승인 상태'가 맞습니까?"
    },
    {
      "id": "H-C03",
      "decision": "구체화 필요",
      "reader_must_infer": "판정 대상(연구 참여 여부 등)이 무엇인지",
      "suggested_revision": "연구 참여 여부는 환자 직접 동의, 연구 제외 등록, 기관 동의, 기본 제외 순으로 판정하며, 동의보다 제외 설정을 우선하여 최종 제외 여부를 결정합니다.",
      "verification_question": "판정 대상이 '연구 참여/제외 여부'가 맞습니까?"
    },
    {
      "id": "H-N01",
      "decision": "구체화 필요",
      "reader_must_infer": "주체와 서술어가 생략되어 있어, 이것이 작업 순서인지 시스템의 자동 동작인지",
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
