- 동기(Synchronous)

  - 모든 일을 순서대로 하나씩 처리
  - 요펑을 보내고 응답이 올때까지 기다렸다가 다음 로직을 처리

- 비동기(Asynchronous)

  - 작업을 시작한 후 결과를 기다리지 않고 다음 작업을 처리
  - 병렬적 수행
  - 시간이 필요한 작업들은 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리
  - 사용자 경험을 위해 비동기를 사용
    - 비동기로 처리한다면 먼저 처리되는 부분부터 보여줄 수 있으므로 긍정적
  - JavaScript의 비동기 처리
    - JavaScript는 한 번에 하나의 일만 수행할 수 있는 Single Thread 언어
    - 즉, JavaScript는 하나의 작업을 요청한 순서대로 처리할 수 밖에 없음
    - JavaScript Runtime
      - JavaScript 자체는 Single Thread이므로 비동기 처리를 할 수 있도록 도와주는 환경이 필요
      - 비동기와 관련한 작업은 브라우저 또는 Node 환경에서 처리
    1. 모든 작업은 Call Stack(LIFO)으로 들어간 후 처리
    2. 오래 걸리는 작업이 Call Stack으로 들어오면 Web API로 보내서 처리
    3. Web API에서 처리가 끝난 작업들은 Task Queue(FIFO)에 순서대로 들어감
    4. Event Loop가 Call Stack이 비어 있는 것을 체크하고, Task Queue에서 가장 오래된 작업을 Call Stack으로 보냄
    - Call Stack
      - 요청이 들어올 때 마다 순차적으로 처리하는 Stack(LIFO)
      - 기본적인 JavaScript의 Singl Thread 작업 처리
    - Web API
      - JavaScript 엔진이 아닌 브라우저에서 제공하는 runtime 환경
      - 시간이 소요되는 작업을처리
      - setTimeout, DOM event, AJAX 요청 등
    - Task Queue
      - 비동기 처리된 Callback 함수가 대기하는 Queue(FIFO)
    - Event Loop
      - Call Stack과 Task Queue를 지속적으로 모니터링
      - Call Stack이 비어 있다면 Task Queue에서 대기 중인 오래된 작업을 Call Stack으로 Push

- Axios

  - JavaScript의 HTTP 웹 통신을 위한 라이브러리
  - 인터페이스와 쉽게 사용할 수 있는 비동기 통신 기능을 제공
  - node 환경은 npm을 이용해 설치 후 사용, browser 환경은 CDN을 이용해서 사용
  - get, post 등 여러 method 사용가능
  - then을 이용해 성공하면 수행할 로직 작성
  - catch를 이용해 실패하면 수행할 로직 작성

- 콜백 함수(Callback Function)

  - 다른 함수의 인자로 전달되는 함수
  - 비동기 처리는 개발자 입장에서 코드의 실행 순서가 불명확하므로 실행 결과를 예상하면서 코드를 작성할 수 없게 함
  - 비동기 콜백(asynchronous callback)
    - 비동기 작업이 완료된 후 실행할 작업을 명시하는 데 사용
    - 비동기 처리를 순차적으로 동작할 수 있게 함
    - 콜백 지옥(Callback Hell)
      - Pyramid of doom(파멸의 피라미드)
      - 비동기 처리를 위한 콜백을 작성할 때 마주하는 문제
      - 코드의 가독성을 해치고 유지 보수가 어려워짐

- 프로미스(Promise)

  - Callback Hell 문제를 해결하기 위해 등장한 비동기 처리를 위한 객체
  - 비동기 작업의 완료 또는 실패를 나타내는 객체
  - Axios 라이브러리가 바로 Promise 기반의 클라이언트
  - `then(callback)`
    - 성공에 대한 약속
    - 요청한 작업이 성공하면 callback 실행
    - callback은 이전 작업의 성공 결과를 인자로 전달 받음
  - `catch(callback)`
    - 실패에 대한 약속
    - then()이 하나라도 실패하면 callback 실행
    - callback은 이전 작업의 실패 객체를 인자로 전달 받음
  - then과 catch는 모두 항상 promise 객체를 반환하므로 계속해서 chaining을 할 수 있음
  - axios로 처리한 비동기 로직이 항상 promise 객체를 반환하므로 then을 계속 이어 나가면서 작성할 수 있음

- AJAX

  - Asynchronous Javascript And XML
  - 비동기 통신 웹 개발 기술
  - 페이지 새로고침 없이 서버에 요청
  - 서버로부터 응답(데이터)를 받아 작업을 수행
  - 이러한 비동기 웹 통신을 위한 라이브러리 중 하나가 Axios

- 팔로우(follow)

  - script 코드를 작성하기 위한 block tag 영역 작성
  - axios CDN 작성
  - form 요소의 action과 method 속성은 삭제하고 요소 선택을 위해 id 속성 지정 및 선택
    - 요청은 axios로 대체됨
  - form 요소에 이벤트 핸들러 작성 및 기존 submit 이벤트 취소
  - axios 요청
    - url에 작성할 user pk 작성
      - `data-*`
        - 사용자 지정 데이터 특성을 만들어 임의의 데이터를 HTML과 DOM 사이에서 교환 할 수 있는 방법
        - data-test-value 라는 이름의 특성을 지정했다면 JavaScript에서는 element.dataset.testValue로 접근
      - [docs](https://developer.mozilla.org/ko/docs/Web/HTML/Global_attributes/data-*)
    - scrftoken
      - hidden 타입으로 숨겨져있는 csrf 값을 가진 input 태그를 선택
      - `[name=csrfmiddlewaretoken]`
      - [docs](https://docs.djangoproject.com/en/3.2/ref/csrf/#ajax)
  - axios 요청을 통해 받는 response 객체를 활용해 view 함수를 통해서 팔로우 여부를 파악할 수 있는 변수를 담아 JSON 타입으로 응답
  - 팔로워 & 팔로잉 수 비동기 적용
    - 요소를 선택할 수 있도록 span 태그와 id 속성 작성
    - 작성한 span 태그를 각각 선택
    - 연산은 view 함수에서 진행하여 결과를 응답으로 전달
    - 응답한 연산 결과를 사용해 각 태그의 인원 수 값 변경

- 좋아요(like)

  - 팔로우와 동일한 흐름 + `forEach()` + `querySelectorAll()`
    - index 페이지 각 게시글에 좋아요 버튼이 있기 때문
