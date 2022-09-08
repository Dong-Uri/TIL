- Database
    - 체계화된 데이터의 모임
    - 조직화된 데이터를 수집하는 저장 시스템

    - 스키마(Schema)
        - 뼈대(Structure)
        - 자료의 구조, 표현 방법, 관계 등을 정의한 구조

    - 테이블(Table)
        - 관계(Relation)
        - 필드와 레코드를 사용해 조직된 데이터 요소들의 집합

        - 필드(field)
            - 속성, 컬럼(Column)
            - 각 필드에는 고유한 데이터 형식이 지정됨

        - 레코드(record)
            - 튜플, 행(Row)
            - 테이블의 데이터가 저장됨

    - PK(Primary Key)
        - 기본 키
        - 각 레코드의 고유한 값
            - 식별자로 사용
        - 다른 항목과 절대로 중복되어 나타날 수 없는 단일 값(unique)

    - 쿼리(Query)
        - 데이터를 조회하기 위한 명령어
        - 조건에 맞는 데이터를 추출하거나 조작하는 명령어
        - Query를 날린다 == 데이터베이스를 조작한다

- Django는 Model을 통해 데이터에 접속하고 관리
- 저장된 데이터베이스의 구조 (layout)
- 각각의 모델은 하나의 데이터베이스 테이블에 매핑(mapping)
    - 하나의 값을 다른 값으로 대응시키는 것

- models.py 작성
    - 모델 **클래스**를 작성
    - 데이터베이스 테이블의 스키마를 정의하는 것
    - `class <app_name>(models.Model):`
        - 각 모델은 models.Model 클래스의 서브 클래스로 표현되므로 상속받아 구성
    - `<클래스 변수> = models.<Field>()`
        - 어떤 타입의 DB 필드(컬럼)을 정의할 것인지 정의
        - 클래스 변수(속성)명
            - DB 필드의 이름
        - 클래스 변수 값
            - models 모듈의 Field 클래스
            - DB 필드의 데이터 타입
    - Django Model Field
        - 필드(컬럼)에 저장할 데이터 유형을 정의
        - [필드 목록](https://docs.djangoproject.com/en/3.2/ref/models/fields/)
        - `CharField(max_length=None, **options)`
            - 길이의 제한이 있는 문자열을 넣을 때 사용
            - max_length
                - 필드의 최대 길이(문자)
        - `TextField(**options)`
            - 글자의 수가 많을 때 사용
            - max_length 옵션이 입력 단계에서는 반영되지만 유효성 검증을 하지 않고 데이터베이스단계에는 적용되지 않음
        - `DateTimeField()`
            - 날짜 및 시간을 값으로 사용하는 필드
            - auto_now_add
                - 최초 생성 일자
            - auto_now
                - 최종 수정 일자
        - `DataField()`, `IntegerField()` 등
    - models.py는 데이터베이스 스키마를 설계한 것

- Migrations
    - Django가 모델에 생긴 변화를 DB에 반영하는 방법
    - `python manage.py makemigrations`
        - 새로운 migation(설계도,청사진)을 만들 때 사용
        - migrations에 네자리 숫자로 시작하는 파이썬 파일 생성
    - `python manage.py migrate`
        - 위에서 만든 설계도를 실제 db.sqlite3 DB 파일에 반영하는 과정
        - 모델과 DB의 동기화
    - 기타
        - `showmigrations`
            - migrations 파일들이 migrate 됐는지 확인
        - `sqlmigrate <app_name> <0000>`
            - 해당 migrations 파일이 SQL 문으로 어떻게 해석 되는지 확인
    - 추가 필드정의
        - models.py에 변경사항이 생기면 위 과정을 다시 진행
        - 이미 존재하는 테이블에 새로운 컬럼이 추가되므로 기본 값을 설정해야 하므로 어떤 값을 설정할 것인지 물어봄
        - 1번을 고르면 그 필드에 대한 default값 설정

- ORM
    - Object-Relational-Mapping
    - 호환되지 않는 Django와 SQL 간에 데이터를 변환하는 프로그래밍 기술
    - SQL을 잘 몰라도 DB 조작 가능
    - 완전한 서비스를 구현하기 어려운 경우도 존재
    - **생산성**
        - 객체 지향적 접근으로 인해 높은 생산성