- [인증 관련 Built-in forms](https://docs.djangoproject.com/en/3.2/topics/auth/default/#module-django.contrib.auth.forms)

- Login
    - Session을 CREATE
    ```python
    from django.contrib.auth.forms import AuthenticationForm
    from django.contrib.auth import login as auth_login

    def login(request):
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            # form = AuthenticationForm(request,data=request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect('articles:index')
        else:
            form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/login.html', context)
    ```
    - `AuthenticationForm`
        - 로그인을 위한 built-in form
        - request를 첫번째 인자로 취함
    - `login(request, user, backend=None)`
        - 인증된 사용자를 로그인 시키는 로직
        - view 함수와 충돌을 방지하기 위해 auth_login으로 변경해서 사용
    - `get_user()`
        - AuthenticationForm의 인스턴스 메서드
        - 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환
    - django_session 테이블의 session_key와 Cookies 내의 sessionid에서 세션 데이터를 확인할 수 있음

- 인증 관련 데이터 출력
    - base.html 에서 `{{ user }}` 사용
        - setting.py의 context processors 설정 값 때문에 context 데이터 없이도 user 변수 사용 가능
            - 템플릿이 렌더링 될 때 호출 가능한 컨텍스트 데이터 목록
            - user 변수를 담당하는 프로세서는 django.contrib.auth.context_processors.auth
                - 현재 로그인한 사용자를 나타내는 User 클래스의 인스턴스가 {{ user }}에 저장됨
                - 로그인 하지 않은 경우 AnonymousUser 클래스의 인스턴스로 생성

- Logout
    - Session을 DELETE
    ```python
    from django.contrib.auth import logout as auth_logout

    def logout(request):
        auth_logout(request)
        return redirect('articles:index')
    ```
    - `logout(request)`
        - 현재 요청에 대한 session data를 DB에서 삭제
        - 클라이언트의 쿠키에서도 sessionid를 삭제