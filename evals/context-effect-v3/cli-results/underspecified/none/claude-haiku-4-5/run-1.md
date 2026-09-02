{
  "cases": [
    {
      "id": "PERM-U",
      "decision": "구체화 필요",
      "evidence_quote": "저장 위치와 자료 구조, 이름, 생성 주체는 아직 결정하지 않았다.",
      "suggested_revision": "권한 정보를 저장할 데이터 구조(예: 권한 테이블, 캐시 키-값 저장소)와 그 생성·갱신 방식을 정의해야 합니다.",
      "verification_question": "문맥에서 '그릇'이 정확히 무엇을 의미하는가? 데이터베이스 테이블, 캐시 저장소, API 응답 형식 등 구체적 대상이 무엇인가?"
    },
    {
      "id": "INV-U",
      "decision": "구체화 필요",
      "evidence_quote": "대응 수단으로 추가 재고, 대체 품목, 복수 공급사, 긴급 운송과 병원 간 전환이 논의됐지만 어느 수단을 어느 품목에 적용할지는 결정되지 않았다.",
      "suggested_revision": "품목별 공급 부족 대응 기준(예: 필수 품목은 추가 재고 + 복수 공급사, 비필수 품목은 대체 품목 우선)을 수립해야 합니다.",
      "verification_question": "'쿠션'이 구체적으로 어떤 메커니즘(안전 재고량, 대체품 확보, 공급사 다변화)을 의미하는가?"
    },
    {
      "id": "STAT-U",
      "decision": "구체화 필요",
      "evidence_quote": "프런트엔드에서 결과를 가져오는 구체적인 API, 상태 관리 방식과 사용자 동작은 아직 합의되지 않았다.",
      "suggested_revision": "통계 결과를 조회하기 위한 API 엔드포인트(예: GET /statistics?region=&policy=&group=), 캐싱 정책(이전 결과 표시 기간), 갱신 트리거(수동/자동)를 정의해야 합니다.",
      "verification_question": "'손잡이'가 API 엔드포인트, UI 제어 버튼, 상태 관리 변수 중 어느 것을 지칭하는가?"
    }
  ]
}
