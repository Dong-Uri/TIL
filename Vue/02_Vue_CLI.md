- Node.js

  - 브라우저가 아닌 환경에서도 자바스크립트를 구동할 수 있게 함
  - Server-Side-Programming 또한 가능해짐
  - NPM(Node Package Manage)
    - Node.js의 기본 패키지 관리자
    - Python에 pip 역할

- Vue CLI

  - Vue 개발을 위한 표준 도구
  - 시작
    - `npm install -g @vue/cli`
      - 설치
    - `vue create vue-cli`
      - 프로젝트 생성
      - vscode terminal에서 진행하여 Vue 버전 선택(Vue 2)
    - `cd vue-cli`
      - 프로젝트디렉토리로 이동 필요
    - `npm run serve`
      - 프로젝트 실행
  - 프로젝트 구조
    - node_modules
      - node.js 한경의 여러 의존성 모듈
      - python의 venv와 비슷한 역할
      - Babel
        - JavaScript compiler
        - ES6+ 코드를 구버전으로 번역/변환 해주는 도구
      - Webpack
        - static module bundler
        - 모듈 간의 의존성 문제를 해결하기 위한 도구
          - 모듈의 수가 많아지고 라이브러리 혹은 모듈 간의 의존성(연결성)이 깊어져 문제 파악이 어려움
        - 다양한 Bundler 중 하나
          - 모듈 의존성 문제를 해결해주는 작업이 Bundling이며 이러한 일을 해주는 도구가 Bundler
    - package.json
      - 프로젝트의 종속성 목록과 지원되는 브라우저에 대한 구성 옵션을 포함
    - package-lock.json
      - node_modules에 설치되는 모듈과 관련된 모든 의존성을 설정 및 관리
      - python의 requirements.txt 역할
    - public/index.html
      - Vue 앱의 뼈대가 되는 html 파일
    - src/
      - src/assets
        - 정적 파일을 저장하는 디렉토리
      - src/components
        - 하위 컴포넌트들이 위치
      - src/App.vue
        - 최상위 컴포넌트
        - public/index.html과 연결
      - src/main.js
        - webpack이 빌드를 시작할 때 가장 먼저 불러오는 entry point
        - public/index.html과 src/App.vue를 연결시키는 작업이 이루어지는 곳
        - Vue 전역에서 활용 할 모듈을 등록할 수 있는 파일

- SFC

  - Single File Component
  - 하나의 .vue 파일이 하나의 Vue instance이고, 하나의 컴포넌트
  - Vue instance에서는 HTML, CSS, JavaScript 코드를 한번에 관리
  - Component
    - UI를 독립적이고 재사용 가능한 조각들로 나눈 것
    - 관리가 용이, 재사용성, 확장 가능, 캡슐화, 독립적
  - Vue component
    - 템플릿(HTML)
      - HTML의 body 부분
      - 눈으로 보여지는 요소 작성
    - 스크립트(JavaScript)
      - JavaScript 코드가 작성되는 곳
      - 컴포넌트 정보, 데이터, 메서드 등 vue 인스턴스를 구성하는 대부분이 작성
    - 스타일(CSS)
      - CSS가 작성되며 컴포넌트의 스타일을 담당
    - 컴포넌트들잉 tree 구조를 이루어 하나의 페이지를 만듦
    - root에 해당하는 최상단의 component가 App.vue이고 이를 index.html과 연결
    - 결국 index.html 파일 하나만을 rendering하는 것이 SPA
    - Vue component 생성
      1. src/components/ 안에 생성
      2. script에 이름 등록
      3. template에 요소 추가
    - Vue component 등록
      1. 불러오기
      - `import {instance name} from {위치}`
      - instance name은 instance 생성 시 작성한 name
      - `@`로 src shortcut 가능
      - `.vue` 생략 가능
      2. 등록하기
      - components에 instance name 추가
      3. 보여주기
      - instance name를 닫는 태그만 있는 요소처럼 사용

- Pass Props

  - 부모에서 자식으로의 데이터 전달 방식
  - 요소의 속성(property)을 사용하여 데이터 전달
  - 요소에 속성을 작성하듯이 사용 가능하며 `prop-data-name="value"`의 형태로 데이터를 전달
    - 이때 속성의 키 값은 kebab-case 사용
  - 데이터를 받는 하위 컴포넌트에서도 전달받은 props를 type과 함께 명시
    - 이때 kebab-case로 넘긴 변수를 자동으로 camelCase로 변환하여 인식함
  - 정적인 데이터를 전달하는 경우 static props라 하며 변수를 전달하는 경우는 dynamic props라 함
    - v-bind directive를 사용해 데이터를 동적으로 바인딩
    - 숫자를 props로 전달하기 위해서는 동적으로 바인딩
  - 단방향 데이터 흐름
    - 부모 속성이 업데이트되면 자식으로 흐르지만 반대 방향은 아님
    - 하위 컴포넌트에서 prop를 변경하려고 시도해선 안되며 Vue는 콘솔에서 경고를 출력

- Emit Event

  - 자식에서 부모로의 데이터 전달 방식
  - `$emit('event-name', 'data')`
    - $emit 메서드를 통해 부모 컴퍼넌트에 이벤트를 발생
    - emit된 이벤트를 상위 컴포넌트에서 청취 후 핸들러 함수 실행
    - 이벤트를 발생(emit)시킬 때 인자로 데이터를 전달 가능
    - 이렇게 전달한 데이터는 이벤트와 연결된 부모 컴포넌트의 핸들러 함수의 인자로 사용 가능
  - pass props와 마찬가지로 동적인 데이터도 전달 가능
