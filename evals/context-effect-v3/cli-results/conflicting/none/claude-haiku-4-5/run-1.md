{
  "cases": [
    {
      "id": "PERM-C",
      "decision": "의미 확인 필요",
      "evidence_quote": "2장에서는 계산된 권한 결과를 `PermissionBundle`이라고 부르며... 4장의 데이터 모델에서는 같은 비유를 `RoleSnapshot` 테이블로 정의한다.",
      "suggested_revision": null,
      "verification_question": "현재 시스템에서 실제로 구현된 권한 저장소가 PermissionBundle(사용자별 JSON)인지 RoleSnapshot(역할별 테이블)인지 확인 필요. 메뉴 API가 호출하는 실제 저장소를 추적할 수 있는가?"
    },
    {
      "id": "INV-C",
      "decision": "의미 확인 필요",
      "evidence_quote": "수요 계획 절에서는 `쿠션`을 A등급 품목의 14일분 안전 재고라고 정의... 조달 운영 절에서는... `쿠션`은 두 번째 공급사와의 긴급 구매 계약을 뜻한다.",
      "suggested_revision": null,
      "verification_question": "현재 운영 중인 정책이 안전 재고 기반인지, 긴급 구매 계약 기반인지 확인 필요. 의사결정 기록에서 최종 승인 상태를 재확인할 수 있는가?"
    },
    {
      "id": "STAT-C",
      "decision": "의미 확인 필요",
      "evidence_quote": "API 절에서는... `usePolicyEffects`가 응답과 갱신을 관리한다고 정의... 상태 관리 절에서는... `PolicyEffectLoader`가 통계를 주입한다고... 클라이언트 훅을 만들지 않으며",
      "suggested_revision": null,
      "verification_question": "현재 배포된 화면의 실제 구현이 React 훅 기반(usePolicyEffects)인지 서버 렌더링 기반(PolicyEffectLoader)인지 확인 필요. 코드 또는 배포 버전에서 어느 아키텍처가 활성화되어 있는가?"
    }
  ]
}
