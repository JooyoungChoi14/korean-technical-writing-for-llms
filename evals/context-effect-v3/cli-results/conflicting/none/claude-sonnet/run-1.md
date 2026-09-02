{
  "cases": [
    {
      "id": "PERM-C",
      "decision": "의미 확인 필요",
      "evidence_quote": "2장에서는 계산된 권한 결과를 `PermissionBundle`이라고 부르며 사용자별 JSON 문서로 저장한다고 정의한다. […] 4장의 데이터 모델에서는 같은 비유를 `RoleSnapshot` 테이블로 정의한다. 이 테이블은 사용자별이 아니라 역할별 행을 가지며 야간 배치가 생성하고 사용자 직접 설정은 포함하지 않는다",
      "suggested_revision": null,
      "verification_question": "최종 설계에서 권한 계산 결과는 PermissionBundle(사용자별 JSON, 로그인 서비스 생성)과 RoleSnapshot(역할별 테이블, 야간 배치 생성) 중 어느 것을 사용하나요?"
    },
    {
      "id": "INV-C",
      "decision": "의미 확인 필요",
      "evidence_quote": "수요 계획 절에서는 `쿠션`을 A등급 품목의 14일분 안전 재고라고 정의하며 병원 창고가 이를 보유한다고 적는다. […] 조달 운영 절에서는 재고를 늘리면 폐기 비용이 커지므로 추가 재고를 두지 않는다고 명시한다. 그 절에서 `쿠션`은 두 번째 공급사와의 긴급 구매 계약을 뜻한다",
      "suggested_revision": null,
      "verification_question": "A등급 품목의 부족 대비책은 14일분 안전재고 보유와 긴급 구매 계약 중 어느 것을 적용하나요?"
    },
    {
      "id": "STAT-C",
      "decision": "의미 확인 필요",
      "evidence_quote": "API 절에서는 화면이 `GET /policy-effects`를 직접 호출하고 React 훅 `usePolicyEffects`가 응답과 갱신을 관리한다고 정의한다. […] 상태 관리 절에서는 브라우저의 직접 호출을 금지하고 서버 렌더링 단계에서 `PolicyEffectLoader`가 통계를 주입한다고 적는다",
      "suggested_revision": null,
      "verification_question": "정책 실험 결과 화면은 클라이언트 훅(usePolicyEffects)으로 직접 API 호출과 서버 렌더링(PolicyEffectLoader)으로 주입 중 어느 방식을 사용하나요?"
    }
  ]
}
