(정리 도움받음)

#1

230228 8기 특화 프로젝트 - 프로젝트 필수 준비과정 : Data Flow & 1주차 News#
목차
✔ 왜 알아야 하는가?
✔ Data Flow 란?
✔ Data Flow 개념'들'
✔ (최소한 한번은 정확히 봐야할) Web Architecture 101
✔ 부록: Architect 의 영역과 역할

Data Flow
✔ 왜 알아야 하는가?
더 좋은 개발자가 되기 위해
보다 정확한 개발을 하기 위해
회의시간의 내용을 빠르게 이해할 수 있기 위해
개발기간을 단축하기 위해
…
✔ Data Flow란?
3 tier model

WEB - SERVER - DB

Presentation tier - Logic Tier Application tier - Data tier

✔ Data Flow 개념 - Monolithic Architecture of Three Tier
JPA, MyBatis, elasticsearch는 미들웨어

장점 : 세세하게 ctrl 가능

단점: 해야할 작업이 많다

✔ Data Flow 개념 - Micro Service Architecture
도커

장점: 편하다

단점: 도커 내 발생 이슈에 대해 해결하기 어렵다

컨설턴트님은 Monolithic 선호

도커가 훨씬 편한데 Native후 docker로 가면 해결 능력이 있는데 바로 docker부터 사용하면 해결하기가 어렵다.

✔ Data Flow 개념 - DevOps
무한으로 동작하는 과정

빌드가 끝난다 → 끝나면? → 또 빌드가 시작

뱀부 젠킨스 아르고 AWS 파이프라인

GitLab은 어디에 있을까? 어플리케이션 티어, 데이터는 데이터 티어에

✔ Data Flow 개념 - Decentralization (BlockChain)
대다수의 모델을 3티어 모델로 설명할 수 있다

✔ (최소한 한번은 정확히 봐야할) Web Architecture 101
https://scvgoe.github.io/2018-12-25-%EB%B2%88%EC%97%AD-Web-Architecture-101/

Architect (설계자)의 종류와 역할
✔ 부록 : Architect의 영역과 역할
https://youngclown.github.io/2018/07/Architect

#2

프로젝트 필수 준비과정 : Data Flow
서성수 컨설턴트님

왜 알아야 하는가?
더 좋은 개발자가 되기 위해
보다 정확한 개발을 하기 위해
회의시간의 내용을 빠르게 이해할 수 있기 위해
개발기간을 단축하기 위해
…
→ 개발자라면 고객의 요청을 이해하고 분석하고 나누어 예측하는 설계 능력이 있어야한다!

Data Flow란?
Three Tier
Presentation (Web)
Logic / Application (Server)
Data (DB)
대부분의 구조를 three tier로 분석 가능
Data Flow 개념’들’
Monolithic Architecture of Three Tier
Micro Service Architecture
DevOps
Decentralization (BlockChain)
Summary
LOG4J: user, request, response 등을 기록 / 실무 레벨에서 outbound는 error level만 기록 / 문제 상황 시 아주 잠깐 inbound에서 info나 debug 레벨까지 기록하기도 함
(최소한 한 번은 정확히 봐야할) Web Architecture 101
Kafka는 6a Job Queue
부록: Architect의 영역과 역할
Appplication Architecture → Web Server
Data Architecture → Dataflow
Technical Architecture → Infra / System

https://medium.com/storyblocks-engineering/web-architecture-101-a3224e126947
