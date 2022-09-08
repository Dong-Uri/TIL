- `python manage.py shell_plus`
    - pip install을 통해 ipython과 django-dxtensions 설치
    - settings.py에 django_extensions를 앱 리스트에 추가
    - django-extension이 제공하는 강력한 shell

- Database API
    - Django가 기본적으로 ORM을 제공함에 따라 DB를 편하게 조작할 수 있도록 도움
    - Model을 만들면 객체들을 읽고 수정하고 지울 수 있는 DB API를 자동으로 만듦
    - `<Model class>.<Manager>.<Queryset API>`
        - `Aricle.objects.all()`
    - `objects` manager
        - DB를 Python class로 조작할 수 있도록 여러 메서드를 제공하는 manager
    - Query
        - 데이터베이스에 특정한 데이터를 보여 달라는 요청
        - 이때 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달
        - 데이터베이스의 응답 데이터를 ORM이 **QuerySet**이라는 자료 형태로 변환하여 전달
    - QuerySet
        - 데이터베이스에게서 전달 받은 객체 목록
        - 필터를 걸거나 정렬 등을 수행할 수 있음
        - 단일한 객체를 반환 할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환됨
    - QuerySet API
        - QuerySet과 상호작용하기 위해 사용하는 도구 (메서드, 연산자 등)

- CRUD
    - Create / Read / Update / Delete
    - 기본적인 데이터 처리 기능 4가지

    - CREATE
        1. 첫번째 방법
            - `<name> = <Model class>()`
                - 클래스를 통한 인스턴스 생성
            - `<name>.<클래스 변수> = ...`
                - 클래스 변수명과 같은 이름의 인스턴스변수를 생성 후 값 할당
            - `<name>.save()`
                - 인스턴스로 save 메서드 호출
                - 호출해야 비로소 DB에 데이터가 저장됨
        2. 두번째 방법
            - `<name> = <Model class>(<클래스 변수>= ..., )`
            - `<name>.save()`
        3. 세번째 방법
            - `<Model class>.objects.create(<클래스 변수>= ..., )`
                - create() 메서드 활용

    - READ
        - all()
            - `<Model class>.objects.all()`
            - 전체 데이터 조회
        - get()
            - `<Model class>.objects.get(<클래스 변수>=...)`
            - 단일 데이터 조회
            - 객체를 찾을 수 없으면 DoesNotExist 예외 발생
            - 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외 발생
            - 그러므로 primary key와 같이 고유성(uniqueness)을 보장하는 조회에서 사용해야 함
        - filter()
            - `<Model class>.objects.filter(<클래스 변수>=...)`
            - 지정된 조회 매개 변수와 일치하는 객체를 포함하는 새 QuerySet을 반환
            - 조회된 객체가 없거나 1개여도 QuerySet을 반환
        - Field lookups
            - 특정 레코드에 대한 조건을 설정하는 방법
            - [lookups 목록](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#field-lookups)

    - UPDATE
        - `<name> = <Model class>.objects.get(<클래스 변수>=...)`
            - 수정하고자 하는 인스턴스 객체를 조회 후 반환 값 저장
        - `<name>.<클래스 변수> = ...`
            - 인스턴스 객체의 인스턴스 변수 값을 새로운 값으로 할당
        - `<name>.save()`
            - save() 인스턴스 메서드 호출

    - DELETE
        - `<name> = <Model class>.objects.get(<클래스 변수>=...)`
            - 삭제하고자 하는 인스턴스 객체를 조회 후 반환 값 저장
        - `<name>.delete()`
            - delete() 인스턴스 메서드 호출

```python
def __str__(self):
    return self.<name>
```
- 위를 모델 클래스에 정의하여 읽을 수 있는 문자열을 반환하도록 할 수 있음