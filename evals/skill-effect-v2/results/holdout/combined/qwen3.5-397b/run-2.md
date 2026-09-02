{
  "cases": [
    {
      "id": "H-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "'관문'이 의미하는 기술 구성 요소 (프록시, API 게이트웨이 등) 와 '둡니다'의 구체적 행위 (설정, 설치, 개방 등)",
      "suggested_revision": "감사 로그를 외부 분석기로 전송하는 중계 지점을 설정합니다.",
      "verification_question": "'관문'이 구체적으로 어떤 기술 구성 요소를 의미하며, 어떤 작업을 수행합니까?"
    },
    {
      "id": "H-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "'쿠션'이 의미하는 완충 장치의 종류 (안전 재고, 시간 여유, 예산 등) 와 '흡수'의 구체적 메커니즘",
      "suggested_revision": "재고 부족 상황을 대비하여 안전 재고량을 확보합니다.",
      "verification_question": "'쿠션'이 안전 재고, 납기 여유,還是 다른 완충 장치를 의미합니까?"
    },
    {
      "id": "H-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "'소켓'이 의미하는 연동 지점 (UI 컴포넌트, API 엔드포인트, DB 컬럼 등) 과 '엽니다'의 행위",
      "suggested_revision": "모델 판정값을 업무 화면에 표시할 연동 지점을 마련합니다.",
      "verification_question": "'소켓'이 화면 UI 의 표시 영역인지, 데이터 연동 인터페이스인지 명확합니까?"
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
      "reader_must_infer": "'순으로 적용'과 '비공개 우선' 규칙이 충돌할 때의 실제 우선순위 결정 로직",
      "suggested_revision": "권한은 현장 관리자, 본사 보안, 문서 소유자 순으로 확인하되, 비공개 조건이 포함되면 공개 조건보다 우선하여 적용합니다.",
      "verification_question": "권한 충돌 시 목록 순서가 우선입니까, 아니면 비공개 조건이 항상 우선입니까?"
    },
    {
      "id": "H-C02",
      "decision": "구체화 필요",
      "reader_must_infer": "'순으로 적용'과 '보류 우선' 규칙이 충돌할 때의 실제 우선순위 결정 로직",
      "suggested_revision": "상태는 긴급 출고 승인, 품질 보류, 영업 승인 순으로 확인하되, 보류 조건이 포함되면 승인 조건보다 우선하여 적용합니다.",
      "verification_question": "상태 충돌 시 목록 순서가 우선입니까, 아니면 보류 조건이 항상 우선입니까?"
    },
    {
      "id": "H-C03",
      "decision": "구체화 필요",
      "reader_must_infer": "'순으로 판정'과 '제외 우선' 규칙이 충돌할 때의 실제 우선순위 결정 로직",
      "suggested_revision": "동의 여부는 환자 직접 동의, 연구 제외 등록, 기관 동의 순으로 확인하되, 제외 조건이 포함되면 동의 조건보다 우선하여 판정합니다.",
      "verification_question": "판정 충돌 시 목록 순서가 우선입니까, 아니면 제외 조건이 항상 우선입니까?"
    },
    {
      "id": "H-N01",
      "decision": "구체화 필요",
      "reader_must_infer": "주체 (시스템 또는 담당자), 시제 (명령, 계획, 기록), 그리고 각 명사구의 서술어 관계",
      "suggested_revision": "결측치를 대치한 후 회귀 모델을 재학습하며, 기존 계수는 폐기합니다.",
      "verification_question": "이 문장이 작업 지시인지, 수행된 작업 기록인지 명확합니까?"
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
