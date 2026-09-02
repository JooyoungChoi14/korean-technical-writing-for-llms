{
  "cases": [
    {
      "id": "PERM-I",
      "decision": "의미 확인 필요",
      "evidence_quote": "이 절에는 권한 계산의 자료 구조나 저장 방식, 생성 주체가 정의되어 있지 않다.",
      "suggested_revision": null,
      "verification_question": "여기서 '그릇'은 권한 정보를 담는 무엇을 가리킵니까? 예를 들어 데이터베이스 테이블, 역할(role) 객체, 세션 내 권한 캐시 중 어느 것이며, 누가 언제 생성하는 구조입니까?"
    },
    {
      "id": "INV-I",
      "decision": "의미 확인 필요",
      "evidence_quote": "이 절은 입력 화면과 동기화 동작만 다루며 부족 상황의 대응 정책이나 보유 수량은 정의하지 않는다.",
      "suggested_revision": null,
      "verification_question": "여기서 '쿠션'은 무엇을 뜻합니까? 안전재고 수량 확보, 부족 시 대체 품목 정책, 자동 발주 트리거 중 어느 것이며, 이 검수 화면 문서에 포함될 내용이 맞습니까?"
    },
    {
      "id": "STAT-I",
      "decision": "의미 확인 필요",
      "evidence_quote": "이 절은 표시와 조작의 접근성만 다루며 통계 값을 가져오는 API나 상태 관리 수단은 정의하지 않는다.",
      "suggested_revision": null,
      "verification_question": "여기서 '손잡이'는 통계 값을 화면에 연결하는 무엇을 가리킵니까? API 호출 함수, 상태 관리의 셀렉터(selector)나 훅(hook) 중 어느 것이며, 접근성 절이 아닌 다른 절로 옮겨야 할 구현 메모입니까?"
    }
  ]
}
