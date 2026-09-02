```json
{
  "cases": [
    {
      "id": "DEV-A01",
      "decision": "구체화 필요",
      "reader_must_infer": "‘다리’가 어떤 컴포넌트나 인터페이스인지, ‘다음 단계’가 어느 처리 단계인지",
      "suggested_revision": "정산 결과를 다음 처리 단계로 전달하는 인터페이스를 추가합니다.",
      "verification_question": "정산 결과를 전달하는 구체적 수단(API, 큐, 파일 등)과 다음 단계의 이름은 무엇입니까?"
    },
    {
      "id": "DEV-A02",
      "decision": "구체화 필요",
      "reader_must_infer": "‘완충지대’가 어떤 예외 처리 구조인지, 예외를 ‘받아낸’ 뒤 어떻게 처리하는지",
      "suggested_revision": "예외를 포착해 처리를 중단하지 않도록 예외 처리 계층을 둡니다.",
      "verification_question": "예외를 포착한 뒤 기록, 무시, 재시도 중 어느 동작을 수행합니까?"
    },
    {
      "id": "DEV-A03",
      "decision": "구체화 필요",
      "reader_must_infer": "‘손잡이’가 어떤 속성이나 API인지, ‘끌어올린다’가 조회인지 렌더링인지",
      "suggested_revision": "화면이 통계 값을 조회할 수 있도록 데이터 조회 속성을 추가합니다.",
      "verification_question": "추가하는 속성이나 API의 이름과 데이터 흐름 방향은 무엇입니까?"
    },
    {
      "id": "DEV-P01",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "DEV-P02",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "DEV-P03",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "DEV-C01",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "DEV-C02",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "DEV-C03",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "DEV-N01",
      "decision": "구체화 필요",
      "reader_must_infer": "주체와 서술어가 빠져 있어 누가 수정 불가하게 만들고 누가 취소 후 재작성하는지",
      "suggested_revision": "월말 마감 이후에는 전표를 수정할 수 없으며, 오류 전표는 취소한 뒤 다시 작성해야 합니다.",
      "verification_question": "전표 수정 제한과 취소 후 재작성을 적용하는 주체(시스템, 사용자, 부서)는 무엇입니까?"
    },
    {
      "id": "DEV-P04",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    },
    {
      "id": "DEV-P05",
      "decision": "통과",
      "reader_must_infer": null,
      "suggested_revision": null,
      "verification_question": null
    }
  ]
}
```
