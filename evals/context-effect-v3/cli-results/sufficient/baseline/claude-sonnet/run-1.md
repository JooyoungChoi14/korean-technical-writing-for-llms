{
  "cases": [
    {
      "id": "PERM-S",
      "decision": "구체화 필요",
      "evidence_quote": "계산된 권한 결과를 `EffectivePermissionSet` 객체 하나로 표현한다.",
      "suggested_revision": "로그인과 권한 변경 시 `PermissionResolver`가 `EffectivePermissionSet` 객체를 생성합니다.",
      "verification_question": null
    },
    {
      "id": "INV-S",
      "decision": "구체화 필요",
      "evidence_quote": "A등급 품목별 `safety_stock_days`를 14로 설정하고, 가용 재고가 이 값 아래로 내려가면 중앙 구매팀에 보충 요청을 보낸다.",
      "suggested_revision": "A등급 품목은 평균 사용량 14일분의 안전 재고를 유지합니다.",
      "verification_question": null
    },
    {
      "id": "STAT-S",
      "decision": "구체화 필요",
      "evidence_quote": "프런트엔드는 이 API 호출과 로딩·오류·마지막 갱신 시각을 관리하는 React 훅 `usePolicyEffects`를 사용한다.",
      "suggested_revision": "`usePolicyEffects` 훅을 추가해 화면이 통계 API를 호출하고 결과를 표시하도록 합니다.",
      "verification_question": null
    }
  ]
}
