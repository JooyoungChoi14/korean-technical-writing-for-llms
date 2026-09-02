{
  "cases": [
    {
      "id": "PERM-S",
      "decision": "구체화 필요",
      "evidence_quote": "권한을 담아낼 그릇이 필요합니다.",
      "suggested_revision": "계산된 권한 결과를 EffectivePermissionSet 객체로 표현합니다.",
      "verification_question": null
    },
    {
      "id": "INV-S",
      "decision": "구체화 필요",
      "evidence_quote": "재고 부족을 흡수할 쿠션이 필요합니다.",
      "suggested_revision": "A등급 품목별 safety_stock_days를 14로 설정하여 평균 사용량 14일분을 추가로 보유합니다.",
      "verification_question": null
    },
    {
      "id": "STAT-S",
      "decision": "구체화 필요",
      "evidence_quote": "통계 값을 화면으로 끌어올릴 손잡이를 추가합니다.",
      "suggested_revision": "GET /policy-effects의 결과를 관리하는 React 훅 usePolicyEffects를 추가합니다.",
      "verification_question": null
    }
  ]
}
