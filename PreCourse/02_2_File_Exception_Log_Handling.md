- 예외 처리

  - try ~ except 문법
    - else와 finally 사용 가능
  - raise 구문
    - 강제로 Exception 발생
  - assert 구문
    - 특정 조건에 만족하지 않을 경우 예외 발생

- File Handling

  - 기본적인 파일의 종류

    - text 파일과 binary 파일

  - Python File I/O

    - 파이썬은 파일 처리를 위해 open 키워드 사용
    - `f = open("<파일이름>", "접근 모드")`
    - 읽기모드
      - `r`
      - read()
        - 파일의 내용을 문자열로 반환
        - with 구문과 함께 사용 가능
      - readlines()
        - 한 줄씩 읽어 List Type으로 반환
    - 쓰기모드, 추가모드
      - `w`, `a`
      - `encoding="utf8"`
      - write()

  - directory 다루기

    - os 모듈을 사용
      - `import os`
    - 최근에는 pathlib 모듈을 사용하여 path를 객체로 다룸
      - `import pathlib`
    - Log 파일 생성
      - 디렉토리가 있는지, 파일이 있는지 확인후 쓰기모드, 추가모드로 파일 생성, 변경

  - Pickle

    - 파이썬의 객체를 영속화(persistence)하는 bulit-in 객체
    - 데이터, object등 실행중 정보를 저장
      - 나중에 불러와서 사용

- Logging Handling

  - Logging

    - 프로그램이 실행되는 동안 일어나는 정보를 기록으로 남기기
    - print
      - print로 남기는 것도 가능하지만 Console 창에만 남기는 기록은 분석시 사용불가

  - logging 모듈

    - `import logging`
    - 프로그램 진행 상황에 따라 다른 Level의 Log를 출력
    - 개발 시점, 운영 시점 마다 다른 Log가 남을 수 있도록 지원
    - debug
      - 개발시 처리 기록을 남겨야하는 로그 정보를 남김
    - info
      - 처리가 진행되는 동안의 정보를 알림
    - warning
      - 사용자가 잘못 입력한 정보나 처리는 가능하나 원래 개발시 의도치 않은 정보가 들어왔을 때 알림
    - error
      - 잘못된 처리로 인해 에러가 났으나, 프로그램은 동작할 수 있음을 알림
    - critical
      - 잘못된 처리로 데이터 손실이나 더이상 프로그램이 동작할 수 없음을 알림

  - configparser

    - 프로그램의 실행 설정을 file에 저장함
    - config file
      - 대괄호로 Section을 나누고 속성은 Key : Value

  - argparser

    - Console 창에서 프로그램 실행시 Setting 정보를 저장함

- Logging formmater

  - Log의 결과값의 format을 지정해줄 수 있음
