- 앱에 초기 데이터(initial data)를 제공
- [docs](https://docs.djangoproject.com/en/3.2/howto/initial-data/#providing-data-with-fixtures)

- 생성(데이터 추출)
    - dumpdata
        - 여러 모델을 하나의 json 파일로 만듦
        - `python manage.py dumpdata <app_name>.<ModelName> > {filename}.json`
        - `--indent 4`로 보기 json을 보기 좋게 만들 수 있음
        - 모델을 한꺼번에 쓰거나 생략하여 모든 모델을 json 파일로 만들 수 있음

- 로드(데이터 입력)
    - loaddata
        - 데이터베이스로 로드
        - `python manage.py loaddata <data>.json`
        - 기본 경로
            - `<app_name>/fixtures/`
        - loaddata를 하나씩 실행하는 경우 모델 관계에 따라 순서가 중요함
            - 참조할 key가 필요한 경우가 있으므로
            - 현재 모델에서는 user, article, comment 순으로 data를 넣어야 함
        - encoding codec 관련 에러 발생 시
            1. dumpdata시 추가 옵션 작성
                - `python -Xutf8 manage.py dumpdata ...`
            2. 메모장 활용
                - json파일을 열어 인코딩을 UTF8로 설정하여 저장