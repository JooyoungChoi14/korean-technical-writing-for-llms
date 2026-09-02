{
  "cases": [
    {
      "id": "PERM-I",
      "decision": "구체화 필요",
      "evidence_quote": "이 절에는 권한 계산의 자료 구조나 저장 방식, 생성 주체가 정의되어 있지 않다. 다만 이전 설계 회의에서 옮겨 온 다음 문장이 배포 체크리스트 아래에 남아 있다.",
      "suggested_revision": "권한 정보를 저장할 데이터베이스 테이블 또는 객체 모델을 정의합니다.",
      "verification_question": "권한 데이터를 어떤 형태(테이블, 캐시, 객체)로 저장할 예정인가요?"
    },
    {
      "id": "INV-I",
      "decision": "구체화 필요",
      "evidence_quote": "이 절은 입력 화면과 동기화 동작만 다루며 부족 상황의 대응 정책이나 보유 수량은 정의하지 않는다. 화면 설명 끝에 다음 문장이 섞여 있다.",
      "suggested_revision": "부족 발생 시 대응 정책(예: 최소 재고 수준, 자동 발주 기준)을 정의합니다.",
      "verification_question": "재고 부족 시 어떤 조치(알림, 자동 발주, 대체 품목 제안 등)를 취할 예정인가요?"
    },
    {
      "id": "STAT-I",
      "decision": "구체화 필요",
      "evidence_quote": "이 절은 표시와 조작의 접근성만 다루며 통계 값을 가져오는 API나 상태 관리 수단은 정의하지 않는다. 끝부분에 다음 구현 메모가 남아 있다.",
      "suggested_revision": "통계 값을 가져올 API 엔드포인트와 프런트엔드 상태 관리 방식(Redux, Context API 등)을 정의합니다.",
      "verification_question": "통계 데이터를 어떤 API에서 가져오며, 화면에서 어떤 상태 관리 라이브러리를 사용할 예정인가요?"
    }
  ]
}
