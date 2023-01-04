- 스택(Stack)

  - 나중에 넣은 데이터를 먼저 반환하도록 설계된 메모리 구조
  - LIFO
  - 입력은 Push, 출력은 Pop
  - 리스트를 사용하여 구현 가능
    - push는 append(), pop은 pop() 이용

- 큐(Queue)

  - 먼저 넣은 데이터를 먼저 반환하도록 설계된 메모리 구조
  - FIFO
  - 입력은 Put, 출력은 Get
  - 리스트를 사용하여 구현 가능
    - put은 append(), get은 pop(0) 이용

- 튜플(Tuple)

  - 값의 변경이 불가능한 리스트
  - `()`를 이용하여 선언
  - 리스트의 연산, 인덱싱, 슬라이싱 동일하게 사용 가능

- 집합(Set)

  - 값을 순서없이 저장, 중복 불허하는 자료형
  - set 객체 선언하여 생성
  - 다항한 집합연산 가능

- 사전(Dictionary)

  - 데이터를 저장 할 때 구분 지을 값을 함께 저장
  - Key 값을 활용하여 Value를 관리

- collections

  - `from collections import -`

  - deque

    - Stack과 Queue 지원 모듈
    - list보다 빠름
    - Linked List의 특성을 지원
    - rotate, append, appendleft, extent, extentleft, pop, popleft

  - defaultdict

    - lambda 함수를 이용하여 기본값을 넣을수 있음
      - 개수를 셀때 초기값을 0으로 설정하는 식으로 활용 가능

  - Counter

    - Sequence type의 data element들의 갯수를 dict 형태로 반환
    - Set의 연산 지원

  - namedtuple

    - Tuple 형태로 Data 구조체를 저장하는 방법
