- 사전 준비
    - sql 파일에서 우클릭 후 Use Database로 사용할 db파일 선택
    - 우클릭 후 Run Selected Query로 실행하고자 하는 명령문 실행

- SQLite Data Types
    - NULL
        - NULL value
        - 정보가 없거나 알 수 없음을 의미
    - INTEGER
        - 정수
    - REAL
        - 실수
    - TEXT
        - 문자 데이터
    - BLOB
        - Binary Large Object
        - 입력된 그대로 저장된 데이터 덩어리
        - 바이너리 등 멀티미디어 파일
    - 별도의 Boolean 타입이 없어 대신 정수 0과 1로 저장됨
    - 날짜 및 시간을 저장하기 위한 타입이 없어  SQLite의 built-in "Date And Time Functions"로 값을 저장
    - SQLite는 다른 정적이고 엄격한 타입(static, rigid typing)이 아닌 동적 타입 시스템(dynamic type system)을 사용
        - 컬럼에 저장된 값에 따라 데이터 타입이 결정됨
        - 다른 데이터베이스와의 호환성 문제가 있기 때문에 테이블 생성 시 데이터 타입을 지정하는 것을 권장
    - Type Affinity
        - 타입 선호도
        - SQLite의 5가지 데이터 타입이 아닌 다른 데이터 타입을 선언하면 각 타입의 지정된 선호도에 따라 인식됨
        - 다른 데이터베이스 엔진 간의 호환성을 최대화하기 위함

- Constraints
    - 제약조건
    - 입력하는 자료에 대해 제약을 정함
    - 데이터 무결성
        - 데이터에 대한 정확성, 일관성을 보장하기 위해 제한을 두어 데이터를 보증하는 것
    - NOT NULL
        - 컬럼이 NULL 값을 허용하지 않도록 지정
    - UNIQUE
        - 컬럼의 모든 값이 서로 구별되거나 고유한 값이 되도록 함
    - PRIMARY KEY
        - 테이블에서 행의 고유성을 식별하는 데 사용되는 컬럼
        - 각 테이블에는 하나의 기본 키만 있음
        - 암시적으로 NOT NULL 제약 조건이 포함됨
    - AUTOINCREMENT
        - 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지
        - Django에서 테이블 생성 시 id 컬럼에 기본적으로 사용하는 제약조건
    - rowid의 특징
        - 테이블을 생성할 때마다 rowid라는 암시적 자동 증가 컬럼이 자동으로 생성됨
        - 새 행을 삽입할 때마다 정수 값을 자동으로 할당
            - 값은 1에서 시작
            - 테이블에서 가장 큰 rowid보다 하나 큰 다음 순차 정수를 자동으로 할당

- CREATE TABLE
    - 데이터베이스에 새 테이블을 만듦
    - id 컬럼은 직접 기본 키 역할의 컬럼을 정의하지 않으면 자동으로 rowid라는 컬럼으로 만들어짐
    ```sql
    CREATE TABLE contacts (
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        email TEXT NOT NULL UNIQUE
    );
    ```

- ALTER TABLE
    - 기존 테이블의 구조를 수정(변경)
    - ALTER TABLE RENAME
    - ALTER TABLE RENAME COLUMN
    - ALTER TABLE ADD COLUMN
        - 테이블에 기존 데이터가 있는 경우 추가되는 컬럼에 값이 없기 때문에 NULL이 작성되는데 NOT NULL 제약조건이 있으면 에러가 발생함
        - DEFAULT 제약 조건을 사용하여 기존 데이터들에게 컬럼값을 주어 해결할 수 있음
    - ALTER TABLE DROP COLUMN
        - FOREIGN KEY(외래 키) 제약조건에서 사용되는 경우, PRIMARY KEY인 경우, UNIQUE 제약 조건이 있는 경우 삭제 불가
    ```sql
    ALTER TABLE table_name RENAME TO new_table_name;
    ALTER TABLE table_name RENAME COLUMN column_name TO new_column_name;
    ALTER TABLE table_name ADD COLUMN column_definition;
    ALTER TABLE table_name DROP COLUMN column_name;
    ```

- DROP TABLE
    - 데이터베이스에서 테이블을 제거