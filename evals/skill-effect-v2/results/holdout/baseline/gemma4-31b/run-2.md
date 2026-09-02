```json
{
  "cases": [
    {
      "id": "H-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "관문이라는 비유가 구체적으로 어떤 기술적 구성 요소(Proxy, API Gateway, Message Queue 등)를 의미하는지, 데이터 전송 방식은 무엇인지",
      "suggested_revision": "감사 로그를 외부 분석기로 전송하기 위한 전송 모듈(또는 게이트웨이)을 구현합니다.",
      "verification_question": "관문이 의미하는 구체적인 컴포넌트나 인터페이스는 무엇입니까?"
    },
    {
      "id": "H-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "쿠션이라는 비유가 버퍼(Buffer), 여유 재고(Safety Stock), 또는 대기 큐(Queue) 중 무엇을 의미하는지",
      "suggested_revision": "재고 부족 시 서비스 중단을 방지하기 위해 일정량의 여유 재고(또는 버퍼)를 확보해야 합니다.",
      "verification_question": "쿠션이 의미하는 것이 물리적 여유 재고입니까, 아니면 시스템상의 버퍼입니까?"
    },
    {
      "id": "H-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "소켓을 연다는 비유가 API 엔드포인트를 추가하는 것인지, UI 컴포넌트의 슬롯을 만드는 것인지, 혹은 특정 인터페이스를 정의하는 것인지",
      "suggested_revision": "모델 판정값을 업무 화면에 표시할 수 있도록 데이터 인터페이스(또는 API 엔드포인트)를 추가합니다.",
      "verification_question": "소켓을 연다는 것이 API 제공을 의미합니까, 아니면 UI 상의 표시 영역 확보를 의미합니까?"
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
      "reader_must_infer": "적용 대상(권한, 접근 제어 등)이 무엇인지, 그리고 '순으로 적용'한다는 것이 우선순위인지 평가 순서인지",
      "suggested_revision": "접근 권한은 현장 관리자(공개), 본사 보안(비공개), 문서 소유자(공개), 기본(비공개) 순으로 확인하며, 설정 중 '비공개'가 하나라도 있으면 최종적으로 비공개 처리합니다.",
      "verification_question": "적용 대상이 '문서 접근 권한'이 맞습니까? 또한 '비공개 우선'의 정확한 논리(OR 조건 등)는 무엇입니까?"
    },
    {
      "id": "H-C02",
      "decision": "구체화 필요",
      "reader_must_infer": "적용 대상(승인 상태, 출고 가능 여부 등)이 무엇인지, '보류를 승인보다 우선'한다는 것이 상태 결정의 우선순위인지",
      "suggested_revision": "출고 상태는 긴급 출고 승인, 품질 보류, 영업 승인, 기본 거절 순으로 판정하며, '보류' 상태가 '승인' 상태보다 우선하여 적용됩니다.",
      "verification_question": "판정 대상이 '출고 가능 여부'가 맞습니까? 보류가 승인보다 우선한다는 것이 최종 상태를 '보류'로 결정한다는 의미입니까?"
    },
    {
      "id": "H-C03",
      "decision": "구체화 필요",
      "reader_must_infer": "판정 대상(참여 적격성, 동의 여부 등)이 무엇인지, '제외를 동의보다 우선'한다는 논리적 결과가 무엇인지",
      "suggested_revision": "연구 참여 여부는 환자 직접 동의, 연구 제외 등록, 기관 동의, 기본 제외 순으로 판정하며, '제외' 조건이 충족되면 '동의' 여부와 상관없이 최종 제외 처리합니다.",
      "verification_question": "판정 대상이 '연구 참여 적격성'이 맞습니까? 제외 우선의 정확한 동작 방식은 무엇입니까?"
    },
    {
      "id": "H-N01",
      "decision": "구체화 필요",
      "reader_must_infer": "주체와 동작이 생략된 명사 나열. 누가/무엇이 대치하고 학습하며 폐기하는지",
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
