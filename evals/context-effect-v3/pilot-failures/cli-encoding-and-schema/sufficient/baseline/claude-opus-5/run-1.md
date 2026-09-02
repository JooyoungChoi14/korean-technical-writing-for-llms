{
  "results": [
    {
      "id": "PERM-S",
      "verdict": "구체화 필요",
      "rubric_category": "동작을 대신하는 비유",
      "reader_must_infer": "'그릇'이 어떤 자료 구조인지, 누가 만들고 무엇을 담으며 어디에 보관되는지가 문장에 없어 독자가 앞 절에서 대상과 동작을 복원해야 한다.",
      "evidence_quote": "개편안에서는 계산된 권한 결과를 `EffectivePermissionSet` 객체 하나로 표현한다.",
      "suggested_revision": "메뉴를 열 때마다 권한을 다시 합산하지 않도록, 계산된 권한 결과를 담는 `EffectivePermissionSet` 객체가 필요합니다. 이 객체는 `PermissionResolver`가 생성하고 세션 저장소에는 식별자만 보관합니다.",
      "semantic_risk": "원문은 필요성만 진술하므로 생성 주체·저장 위치를 수정문에 넣으면 문맥의 다른 문장을 요약에 끌어오는 것이다. 주체를 넣지 않으려면 첫 문장만 사용한다.",
      "facts_to_verify": []
    },
    {
      "id": "INV-S",
      "verdict": "구체화 필요",
      "rubric_category": "동작을 대신하는 비유",
      "reader_must_infer": "'쿠션'이 어떤 수량인지, 어느 등급 품목에 얼마만큼 적용되는지, 부족 시 어떤 동작이 일어나는지가 문장에 없다.",
      "evidence_quote": "각 병원은 A등급 품목별 `safety_stock_days`를 14로 설정하고, 가용 재고가 이 값 아래로 내려가면 중앙 구매팀에 보충 요청을 보낸다.",
      "suggested_revision": "공급사 납기가 지연되어도 A등급 품목의 진료가 중단되지 않도록, 품목별로 평균 사용량 14일분의 안전 재고가 필요합니다.",
      "semantic_risk": "'납기 지연의 95%를 감당'은 관측 데이터에 근거한 추정치이므로, 수정문에서 무조건 중단이 없다는 단정으로 바뀌지 않도록 범위를 A등급으로 한정했다.",
      "facts_to_verify": []
    },
    {
      "id": "STAT-S",
      "verdict": "구체화 필요",
      "rubric_category": "동작을 대신하는 비유",
      "reader_must_infer": "'손잡이'가 어떤 코드 구성 요소인지, 값이 어느 방향으로 흐르는지, 어떤 시점에 동작하는지가 문장에 없다.",
      "evidence_quote": "프런트엔드는 이 API 호출과 로딩·오류·마지막 갱신 시각을 관리하는 React 훅 `usePolicyEffects`를 사용한다.",
      "suggested_revision": "화면이 `GET /policy-effects`의 결과를 읽을 수 있도록, API 호출과 로딩·오류 상태를 관리하는 `usePolicyEffects` 훅과 재조회용 `reload` 함수를 추가합니다.",
      "semantic_risk": "원문의 '끌어올릴'은 화면이 값을 읽는 방향이므로 훅이 화면에 값을 밀어 넣는 표현으로 바꾸지 않았다. 상세 설계가 이미 승인된 상태여서 '추가합니다'가 신규 도입인지 기존 결정의 재진술인지는 확정되지 않는다.",
      "facts_to_verify": [
        "`usePolicyEffects` 훅이 이번 개편에서 새로 추가되는 것인지, 이미 존재하는 것을 요약에서 다시 언급한 것인지"
      ]
    }
  ]
}
