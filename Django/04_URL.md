- Trailing Slashes
    - Django는 URL 끝에 `/`를 붙이는 것이 기본
    - 마찬가지로 배열 끝에 `,`를 붙이는 것을 trailing comma라고 함

- Variable routing
    - URL 주소를 변수로 사용하는 것을 의미
    - 즉, 변수값에 따라 하나의 path()에 여러 페이지를 연결시킬 수 있음
    - 변수는 `<>`에 정의하여 view 함수의 인자로 할당됨
        - 이후 context를 통해 템플릿 변수로 사용할 수 있음
    - `str`, `int`, `slug`, `uuid`, `path` 5가지 타입으로 명시
    - `str`
        - `/`를 제외하고 비어 있지 않은 문자열
        - 작성하지 않을 경우 기본 값
    - `int`
        - 0 또는양의 정수

- URL mapping
    - 앱이 많아졌을 때 urls.py를 각 app에 매핑
    - 각각의 app 폴더 안에 urls.py를 작성
        - 각각 자신의 views를 import 할 수 있음
        - urlpatterns를 빈 리스트라도 작성되어야 함
    - 프로젝트 폴더의 urls.py에서 각 앱의 urls.py로 연결
        - `path('<name>/', include('<name>.urls')),`로 작성
        - include를 path와 함께 import
            - 다른 URLconf들을 참조할 수 있도록 돕는 함수
    - 메인 페이지 주소는 앱 이름이 추가됨

- Naming URL patterns
    - 링크에 URL을 직접 작성하지 않고 path() 함수의 name인자를 정의해서 사용
    - DTL의 Tag중 하나인 URL 태그를 사용해서 path()에 작성한 name 사용 가능
        - `{% url '' %}`
    - URL을 하드 코딩하지 않고도 DRY 원칙을 위반하지 않으면서 링크를 출력
        - Don't Repeat Yourself

- URL namespace
    - 서로 다른 앱에서 동일한 URL 이름을사용하는 경우에도 이름이 지정된 URL을 고유하게 사용 가능
    - urls.py에 app_name attribute를 작성
        - `app_name = '<app_name>'`
    - url 태그에도 app_name을 함께 써줌
        - `{% url '<app_name>:<name>' %}`