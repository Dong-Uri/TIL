- DOM

  - 문서 객체 모델
  - Document Object Model
  - 문서를 논리 트리로 표현
  - 파싱(Parsing)
    - 구문 분석, 해석
    - 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정

- DOM의 주요 객체

  - window
    - DOM을 표현하는 창
    - 가장 최상위 개체
    - 작성시 생략 가능
    - 각각의 탭을 각각의 window 객체로 나타냄
    - `window.open()`
      - 새 탭 열기
    - `winodw.alert()`
      - 경고 대화 상자 표시
    - `window.print()`
      - 인쇄 대화 상자 표시
  - document
    - 브라우저가 불러온 웹 페이지
    - 페이지 컨텐츠의 진입점 역할
    - document는 winodw의 속성
    - `document.title`
      - 현재 문서의 제목
      - HTML의 `<title>` 값

- DOM 조작

  1. 선택(Select)
     - `document.querySelector(selector)`
       - 제공한 선택자와 일치하는 element 한 개 선택
       - 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환
       - 없다면 null 반환
     - `document.querySeletorAll(selector)`
       - 제공한 선택자와 일치하는 여러 element를 선택
       - 매칭 할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
       - 제공한 CSS selector를 만족하는 NodeList를 반환
         - index로만 각 항목에 접근 가능
         - 배열의 forEach 메서드 및 다양한 배열 메서드 사용 가능
         - DOM의 변경사항을 실시간으로 반영하지 않음
  2. 조작(Manipulation)
     - `document.createElement(tagName)` (생성)
       - 작성한 tagName의 HTML 요소를 생성하여 반환
     - `Node.innerText` (입력)
       - Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현
     - `Node.appendChild()` (추가)
       - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입
     - `Node.removeChild()` (삭제)
       - DOM에서 자식 Node를 제거
     - `Element.getAttribute(attributeName)` (속성 조회)
       - 해당 요소의 지정된 값(문자열)을 반환
     - `Element.setAttribute(name, value)` (속성 설정)
       - 지정된 요소의 값을 설정

  - [NodeList mdn](https://developer.mozilla.org/ko/docs/Web/API/NodeList)
  - [classList mdn](https://developer.mozilla.org/ko/docs/Web/API/Element/classList)
