- 데이터 표현을 제어하는 도구이자 표현에 관련된 로직

- Django Template Language (DTL)
    - [공식 문서](https://docs.djangoproject.com/en/3.2/ref/templates/language/)
    - Django template에서 사용하는 built-in template system
    - 조건, 반족, 변수 치환, 필터 등의 기능 제공
    - Variable
        - `{{ variable }}`
        - `.`으로 변수 속성에 접근 가능
        - `render()`의 세번째 인자(*context*)로 딕셔너리 형태로 넘겨주며, key의 문자열이 변수명이 됨
    - Filters
        - `{{ variable|filter }}`
        - 표시할 변수를 수정할 때 사용
        - [내장 필터 목록](https://himanmengit.github.io/django/2018/02/23/Built-In-Template-Filter.html)
    - Tags
        - `{% tag %}`
        - 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
        - [내장 태그 목록](https://himanmengit.github.io/django/2018/02/23/Built-In-Template-Tags.html)
    - Comments
        - `{# #}`
        - 주석을 표현하기 위해 사용
        - 여러 줄 주석
            - `{% comment %}`와 `{% endcomment %}`사이에 입력

- 상속(inheritance)
    - 상속 관련 태그
        - `{% extends '' %}`
            - 자식 템플릿이 부모 템플릿을 확장한다는 것을 알림
            - 반드시 템플릿 최상단에 작성
            - 2개 이상 사용 불가
        - `{% block content %}{% endblock content %}`
            - 하위 템플릿에서 재지정 할 수 있는 블록을 정의
    - 기본적으로 프로젝트 최상단에서 `templates` 폴더안에 `base.html`을 skeleton 템플릿으로 작성
        - 기본 html에 bootstaip CDN등을 작성한후 body내에 block 설정
        - 최상단의 templates 경로를 추가하기 위해 `setting.py`의 TEMPLATES에 `'DIRS': [BASE_DIR / 'templates',]` 설정
            - `BASE_DIR = Path(__file__).resolve().parent.parent`
            - setting.py에서 특정 경로를 절대 경로로 편하게 작성할 수 있도록 미리 지정해둔 경로 값

- Sending form data (Client)
    - `<form>`
        - 데이터가 전송되는 방법을 정의
        - 데이터를 어디(*action*)로 어떤 방식(*method*)으로 보낼지
        - action
            - 입력 데이터가 전송될 URL 지정
            - 지정하지 않으면 현재 form이 있는 페이지의 URL로 보냄
        - method
            - 입력 데이터의 HTTP request methods를 지정
            - 데이터 전송은 GET과 POST 2가지 방식 뿐
            - GET 방식에서는 URL에서 `?key=value&key=value/`형식으로 데이터를 전달
                - `Query String`이라고 함
        - `<input>`
            - type 속성에 따라 동작 방식이 다름
            - [input 유형](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input)
            - name
                - 데이터를 제출했을 때 name에 설정된 값을 서버로 전송하고, 서버는 그 값을 통해 사용자가 입력한 데이터 값에 접근
                - name은 key, value는 value

- Retrieving the data (Server)
    - action이 가르키는 곳에서 데이터를 받음
    - 데이터는 view 함수의 첫번째 인자 *request*에 들어있음
    - `<name> = request.GET.get('<name>')`형식으로 데이터를 받음 (GET 방식)
    - `context = {'<name>': <name>,}`형식으로 보통 context에 다시 저장
    - 이후 템플릿에서 사용

- Template namespace
    - 디렉토리를 생성하여 이름공간을 구분
    - templates의 기본 경로 자체는 변경할 수 없으므로 내부에 app이름의 경로를 더 추가
        - `<app_name>/templates/<app_name>/` 형태
    - 폴더 구조 변경 후 views.py의 경로를 변경된 경로로 수정