- NoReverseMatch 에러
    - url 태그확인

- READ1 (index page)

    - 전체 게시글을 조회해서 출력
        ```python
        def index(request):
            articles = Article.objects.all()
            context = {
                'articles': articles,
            }
            return render(request, 'articles/index.html', context)
        ```
        ```html
        {% for article in articles %}
        <p>{{ article.pk }}</p>
        <p>{{ article.title }}</p>
        <p>{{ article.content }}</p>
        <hr>
        {% endfor %}
        ```

- CREATE

    - 사용자의 입력을 받을 페이즈를 렌더링 하는 함수
        ```python
        def new(request):
            return render(request, 'articles/new.html')
        ```
        ```html
        <form action="{% url 'articles:create' %}" method="POST">
            {% csrf_token %}
            <label></label>
            <input> (name이 'title'과 'content'인)
        </form>
        ```
        - index에 new 페이지로 이동할 수 있는 링크 작성
        
    - HTTP request method
        - GET
            - 특정 리소스를 가져오도록 요청할 때 사용
            - 반드시 데이터를 가져올 때만 사용
            - DB에 변화를 주지 않음
            - CRUD에서 R 역할
            - HTML의 a tag도 GET
        - POST
            - 서버로 데이터를 전송할 때 사용
            - 서버에 변경사항을 만듦
            - HTTP body에 담아 전송
            - URL로 보내지지 않음
            - CRUD에서 C/U/D 역할

    - CSRF
        - Cross-Site-Request-Forgery
        - 사이트 간 요청 위조
        - CSRF 공격 방어
            - Security Token 사용 방식
        - csrf_token 템플릿 태그
            - `{% csrf_token %}`
            - 해당 태그가 없다면 403 forbidden으로 응답
                - 권한 때문에 거절되었다는 것을 의미
            - 템플릿에서 내부 URL로 향하는 POST form을 사용하는 경우에 사용
            - 외부 URL로 향하는 POST form에 대해서는 CSRF 토큰이 유출되어 취약성을 유발할 수 있기 때문에 사용해서는 안됨

    - 사용자가 입력한 데이터를 전송 받아 DB에 저장하는 함수
        ```python
        from django.shortcuts import render, redirect

        def create(request):
            title = request.POST.get('title')
            content = request.POST.get('content')
            # 2번째 방식
            article = Article(title=title, content=content)
            article.save()
            return redirect('articles:detail', article.pk)
        ```
        - 추후 유효성 검사를 위해 2번째 생성 방식 사용
        - redirect
            - 302 status code 응답을 통해 해당 URL 페이지 이동
            - READ2에서 만들 detail 페이지를 해당 pk를 통해 이동

    - HTTP response status code
        - 요청이 성공적으로 완료 되었는지 여부를 알려줌
        1. Infomational responses (1xx)
        2. Successful responses (2xx)
        3. Redirection messages (3xx)
        4. Client error responses (4xx)
        5. Server error responses (5xx)
        - [HTTP 고양이](https://http.cat/)
        - [상태 코드 목록](https://developer.mozilla.org/ko/docs/Web/HTTP/Status)

- READ2 (detail page)

    - 개별 게시글 상세 페이지 제작
    - `path(<'int:pk>/', views.detail, name='detail')`
        - 글의 번호(pk)를 활용해 하나의 뷰 함수와 템플릿 파일로 대응
        - Variable Routing 활용
        ```python
        def detail(request, pk):
            article = Article.objects.get(pk=pk)
            context = {
                'article': article,
            }
            return render(request, 'articles/detail.html', context)
        ```
        - variable routing을 통해 pk를 받음
    - `<a href="{% url 'articles:detail' article.pk %}">`
        - url과 함께 pk를 같이 줌