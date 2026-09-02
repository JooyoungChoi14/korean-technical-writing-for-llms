{
  "cases": [
    {
      "id": "PERM-I",
      "decision": "의미 확인 필요",
      "evidence_quote": "권한 계산의 자료 구조나 저장 방식, 생성 주체가 정의되어 있지 않다. 다만 이전 설계 회의에서 옮겨 온 다음 문장이 배포 체크리스트 아래에 남아 있다.",
      "suggested_revision": null,
      "verification_question": "권한 데이터를 어느 구성 요소가 어떤 형식으로 저장하며, 배포 절차에서 이 정보가 필요한 이유는 무엇입니까?"
    },
    {
      "id": "INV-I",
      "decision": "의미 확인 필요",
      "evidence_quote": "이 절은 입력 화면과 동기화 동작만 다루며 부족 상황의 대응 정책이나 보유 수량은 정의하지 않는다. 화면 설명 끝에 다음 문장이 섞여 있다.",
      "suggested_revision": null,
      "verification_question": "재고 부족 시 어느 모듈이 어떤 동작을 수행하며, 입고 검수 화면과 어떤 관계가 있습니까?"
    },
    {
      "id": "STAT-I",
      "decision": "구체화 필요",
      "evidence_quote": "이 절은 표시와 조작의 접근성만 다루며 통계 값을 가져오는 API나 상태 관리 수단은 정의하지 않는다. 끝부분에 다음 구현 메모가 남아 있다.",
      "suggested_revision": "화면이 통계 값을 읽을 수 있도록 API 또는 상태 속성을 추가합니다.",
      "verification_question": "통계 값을 제공하는 구성 요소는 무엇이며, 화면은 어떤 인터페이스로 값을 읽습니까?"
    }
  ]
}
