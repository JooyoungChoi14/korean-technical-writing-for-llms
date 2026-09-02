{
  "cases": [
    {
      "id": "PERM-C",
      "decision": "의미 확인 필요",
      "evidence_quote": "두 절 모두 현재안으로 표시되어 있고 변경 이력에는 어느 정의가 폐기됐는지 남아 있지 않다.",
      "suggested_revision": null,
      "verification_question": "`그릇`이 가리키는 저장 구조는 로그인 서비스가 사용자별로 생성하는 `PermissionBundle`입니까, 야간 배치가 역할별로 생성하는 `RoleSnapshot`입니까? 메뉴 API는 둘 중 무엇을 읽습니까?"
    },
    {
      "id": "INV-C",
      "decision": "의미 확인 필요",
      "evidence_quote": "문서의 의사결정 기록에는 어느 정책이 최종안인지 표시되지 않았다.",
      "suggested_revision": null,
      "verification_question": "A등급 품목의 부족 대응 최종안은 병원 창고가 보유하는 14일분 안전 재고입니까, 중앙 구매팀이 발동하는 두 번째 공급사 긴급 구매 계약입니까?"
    },
    {
      "id": "STAT-C",
      "decision": "의미 확인 필요",
      "evidence_quote": "변경 이력에는 어느 설계가 폐기됐는지 기록되지 않았다.",
      "suggested_revision": null,
      "verification_question": "통계를 화면에 제공하는 최종 설계는 클라이언트 훅 `usePolicyEffects`가 `GET /policy-effects`를 직접 호출하는 방식입니까, 서버 렌더링 단계에서 `PolicyEffectLoader`가 주입하고 필터 변경 시 전체 페이지를 다시 요청하는 방식입니까?"
    }
  ]
}
