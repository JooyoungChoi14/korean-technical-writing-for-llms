# 내용 판정에서 제외한 실행 실패

이 디렉터리는 스킬 효과가 아니라 실행 환경 때문에 생긴 실패를 보존합니다.

- `concurrency-8-rate-limit`: Ollama Cloud 6개 모델, 동시성 8에서 발생한 429 응답
- `retry-5-still-rate-limited`: 동시성을 3으로 낮추고 최대 5회 재시도한 뒤에도 이어진 429 응답
- `cli-home-and-stderr`: PowerShell 백그라운드 작업에 사용자 홈이 전달되지 않고 표준 오류가 JSON에 섞인 첫 CLI 연동 실패
- `cli-encoding-and-schema`: Windows 출력 인코딩과 Claude의 출력 계약을 바로잡기 전 연동 결과

최종 점수에는 이 파일을 포함하지 않았습니다. 실패를 삭제하지 않은 이유는 제공자 상태, 하네스, 인코딩과 내용 오판을 사후에 구분할 수 있게 하기 위해서입니다.
