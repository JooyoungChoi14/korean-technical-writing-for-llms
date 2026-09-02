{
  "cases": [
    {
      "id": "PERM-C",
      "decision": "의미 확인 필요",
      "evidence_quote": "2장에서는 계산된 권한 결과를 `PermissionBundle`이라고 부르며 사용자별 JSON 문서로 저장한다고 정의한다... 4장의 데이터 모델에서는 같은 비유를 `RoleSnapshot` 테이블로 정의한다... 두 절 모두 현재안으로 표시되어 있고 변경 이력에는 어느 정의가 폐기됐는지 남아 있지 않다.",
      "suggested_revision": null,
      "verification_question": "현재 시스템이 권한 정보를 저장하는 실제 단위는 무엇입니까? 사용자별 문서(`PermissionBundle`)인지 역할별 행(`RoleSnapshot`)인지 확정해 주세요."
    },
    {
      "id": "INV-C",
      "decision": "의미 확인 필요",
      "evidence_quote": "수요 계획 절에서는 `쿠션`을 A등급 품목의 14일분 안전 재고라고 정의하며... 반면 조달 운영 절에서는... `쿠션`은 두 번째 공급사와의 긴급 구매 계약을 뜻하며... 두 절은 모두 승인 완료 상태이고... 문서의 의사결정 기록에는 어느 정책이 최종안인지 표시되지 않았다.",
      "suggested_revision": null,
      "verification_question": "현재 운영 중인 정책은 안전 재고(14일분 병원 창고 보유)인지 긴급 구매 계약(부족 시 중앙 구매팀 발동)인지 확정해 주세요."
    },
    {
      "id": "STAT-C",
      "decision": "의미 확인 필요",
      "evidence_quote": "API 절에서는 화면이 `GET /policy-effects`를 직접 호출하고 React 훅 `usePolicyEffects`가 응답과 갱신을 관리한다고 정의한다... 그러나 상태 관리 절에서는 브라우저의 직접 호출을 금지하고 서버 렌더링 단계에서 `PolicyEffectLoader`가 통계를 주입한다고 적는다... 두 절 모두 승인 상태이고... 변경 이력에는 어느 설계가 폐기됐는지 기록되지 않았다.",
      "suggested_revision": null,
      "verification_question": "현재 선택된 설계는 클라이언트 훅 기반(`usePolicyEffects`)인지 서버 렌더링 기반(`PolicyEffectLoader`)인지 확정해 주세요."
    }
  ]
}
