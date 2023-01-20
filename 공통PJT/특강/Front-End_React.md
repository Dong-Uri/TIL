(정리 도움받음)

#1

0117 Frot-End 개발 시작해보기 - React
Why ~ How
왜 리액트를 쓸까?
리액트의 어려운 점
예전 Vue 인스턴스 : html 템플릿, script, style ⇒ 다가가기 편함, 문법 자체도 html 태그 안에서 커스터마이징 가능했기에 접근성이 편했다.
React : 밑에 jsx문법이 들어가지만, 기본적인 바탕자체가 script 언어를 기반으로 하고 있기에, 화면 기반의 퍼블리셔, 웹 디자인의 경우 리액트는 난해했다.
그러면 지금 가장 많이 쓰이는 리액트에 대해 알아가보자
CRA (react tool)
CRA (Create React App)
babel, webpack
설치 및 시작
Node.js 설치 ( 최신 : 19.3.0)
CRA 설치
npx create-react-app "project name"
index.js
실제로 html을 다루는 곳은 “index.js”
App 컴포넌트 부분에 app.js가 표현이 된다.
App.js
변수 지정과 return
리액트에서 object를 표현하는 방법인 “중괄호 {}”를 기억해라
useState ( Hook )
컴포넌트 내의 데이터를 다룸 ⇒ [객체, 대체값]
let [name, nameUpdate] = useState(["남기성", "A806"]);
vue에서도 store개념으로 hook 기능을 제공하고 있음을 인지하자
component
리액트로 만들어진 앱을 이루는 최소한의 단위
컴포넌트를 쓰기 위해선 props 개념을 사용해야 한다.
컴포넌트를 call하면서 props 문법을 사용해 변수값을 넘겨서 실제로 컴포넌트의 값에 적용됨을 보여줌
DataGrid
데이터 관리를 용이하게 할 수 있는 tool
컴포넌트 형태의 라이브러리를 활용
https://mui.com/
⇒ 수많은 props를 통한 data 정렬 기능 제공

#2

공통 프로젝트 - Front-End 개발 시작해보기 : React 및 2주차 News

1. Why_How
   새로운 언어라는 막연함(GWB -> C -> java(oop) -> PASCAL -> Angular.js -> node.js -> vue(nuxt.js) -> react.js
   ex) Vue

3개의 구조로 이루어짐(html/template)(script)(style)
ex) React

4개의 구조로 이루어짐(React 인스턴스, style, script, html(template)) 2. CRA(Create React App)
babel(es6), webpack(es6)
Node.js 설치(보통은 LTS, 하지만 강사님은 달랐죠 Current 로 다운)
npx create-react-app app_name 명령어 실행하기
npm start 리액트 실행
index.html > App.js > import 하는 routes > import 하는 component
// 기본 입력 형식
const App = () => {
return (

   <div>입력</div>
  )
}
export default App;
3. useState
이벤트에 대한 값을 정확하게 전달하기 위해서 사용하는 기본 훅
ex) const [객체, 대체값] = useState(default);

4. component
   화면을 재사용할 수 있게 여러 조각으로 나눈 걸 컴포넌트
   ex)

function createHeader() {
return (

<div>
<header>
header 부분
</header>
</div>
);
}

export default createHeader;
function createBody() {
return (

<div>
<header>
<h1>본문 부분!!</h1>
</header>
</div>
);
}

export default createBody;
function createFooter() {
return (

<div>
<header>
footer 부분
</header>
</div>
);
}

export default createFooter;
위의 3개 모두가 컴포넌트이고 이를 사용하는 방법은 다음과 같다.

// App.js
import HeaderComponent from "./HeaderComponent";
import BodyComponent from "./BodyComponent";
import FooterComponent from "./FooterComponent";

const App = () => {
return (

<div>
<HeaderComponent/>
<BodyComponent/>
<FooterComponent/>
</div>
);
};

export default App; 5. DataGrid(mui)
npm install @mui/material @emotion/react @emotion/styled : 설치해서 MUI 사용가능
import { DataGrid } from `@mui/x-data-grid';

import React from 'react';
import ReactDOM from 'react-dom';
import DataGrid from '@material-ui/core/Button'; // Button을 import 한다.

function App() {
return (
<DataGrid variant="contained" color="primary"> // 사용한다.
Hello World
</DataGrid>
);
}

ReactDOM.render(<App />, document.querySelector('#app'));
사용법도 쉽습니다.

사용하고자 하는 항목을 import 한다
mui에서 코드 복사해서 붙여넣기
styles을 이용하여 각 component를 커스텀마이징 한다.
이상 리액트 요약이었습니다.

#3

React
Why ~ How
CRA
useState
component
DataGrid
Why?
새로운 언어라는 막연함
눈에 안들어오는 코드의 난해함
How?
CRA(Create React App)
babel
webpack
설치 및 시작
Nodejs설치
Node Package Manager(NPM)
CRA 설치
설치 희망 path 이동
ex) C:\Users\vailish\test>npm create-react-app testpjt
React문법
{ }
{ title[0] }과 같이 써주면 인식함
let title = ['이름', '전공']

// 중략

  <tr>
    <th scope="cols">{ title[0] }</th>
    <th scope="cols">{ title[1] }</th>
  </tr>
// 중략
useState
객체, 대체값
버튼 클릭시 요소가 바뀌게 들어가게 할 수 있음(아래 예시)
import { useState } from 'react';
//중략

let [name, nameUpdate] = useState(['존스노우', '에드 스타크'])

// 중략
<button onClick={ () => { nameUpdate(['아리아', '산사'])}}></button>
// 중략
component
component 재사용
// 생략

<tbody>
{
  name.map((n, i) => {
    return (
      <TrComp name={name[i]} major={major[i]}/>
    )
  })
}
</tbody>
// 중략

//component
fuction TrComp(props) {
return (
<tr>
<th scope="row"> { props.name }></th>
<td>{ props.major }</td>
</tr>
)
}
DataGrid
import { DataGrid } from '@mui/x-data-grid';
// 중략

const columns = [
{ field : 'id', headerName : '사번', width : 90 },
{ field : 'name', headerName : '이름', width : 90 },
{ field : 'teamNo', headerName : '팀', width : 90 },
];

// 중략

return (

  <div className="App">
    <div style ={{ height: 500, width: '100%' }}>
      <DataGrid rows={rows} cloumns={columns}/>
    </div>
  </div>
);
