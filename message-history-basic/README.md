## 1. 메시지 관리

- 아래 명령어를 통해 파이썬 실행
```shell
> pipenv run python message-history-basic.py -m "사용자 메시지" -c "채팅방 ID"
```

<br>

### 채팅방 아이디가 kdg라면 미리 설정해준 메시지를 사용하여 대화

```text
> pipenv run python message-history-basic.py -m "김동균은 주로 어떤 영어 닉네임을 사용할까?" -c "kdg"
김동균은 주로 "woody"라는 영어 닉네임을 사용합니다.

> pipenv run python message-history-basic.py -m "그럼 김동균의 최근 관심사는 뭐야?" -c "kdg"
김동균의 최근 관심사는 LLM(대규모 언어 모델)입니다.

> pipenv run python message-history-basic.py -m "오 그레? 그럼 어떻게 공부하고 있대?" -c "kdg"
김동균의 경우, LLM(대규모 언어 모델)에 관심을 가지고 유데미에서 강의를 통해 공부하고 있다는 정보를 기반으로 말씀드릴 수 있습니다. 유데미는 다양한 온라인 강의를 제공하는 플랫폼이므로, 그는 LLM의 원리, 활용 방법, 또는 관련 기술들을 배우기 위한 수업을 수강하고 있을 것입니다. 또한, 강의가 진행되는 동안 실습이나 프로젝트를 통해 이론을 실제로 적용해보는 경험도 쌓고 있을 가능성이 높습니다.
```