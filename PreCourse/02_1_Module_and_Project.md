- Module 만들기

  - py 파일을 의미
  - import 문을 사용해서 module을 호출

- namespace

  - 모듈을 호출할 때 범위 정하는 방법
  - from과 import 키워드를 사용
  - Alias 설정
    - as를 사용하여 모듈명을 별칭으로

- Built-in Modules

  - 파이썬이 기본 제공하는 라이브러리
  - random, time, urllib.request 등

- package

  - 대형 프로젝트를 만드는 코드의 묶음
  - package namespace
    - 기본적으로 절대참조
    - `.`
      - 현재 디렉토리 기준
    - `..`
      - 부모 디렉토리 기준

- conda 가상환경

  - `conda create -n my_project python=3.8`
    - 가상환경 생성
  - `conda install <패키지명>`
    - 패키지 설치
  - matplotlib
    - 대표적인 파이썬 그래프 관리 패키지
