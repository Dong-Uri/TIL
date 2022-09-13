- Custom user & Built-in auth forms
    - User 모델을 대체해도 커스텀 하지 않아도 사용 가능한 Form 클래스
        - AuthenticationForm
        - SetPasswordForm
        - PasswordChangeForm
        - AdminPasswordChangeForm
    - 커스텀 유저 모델을 사용하려면 다시 작성하거나 확장해야 하는 forms
        - UserCreationForm
        - UserChangeForm
    - forms.py
        ```python
        from django.contrib.auth import get_user_model
        from django.contrib.auth.forms import UserCreationForm, UserChangeForm

        class CustomUserCreationForm(UserCreationForm):

            class Meta(UserCreationForm.Meta):
                model = get_user_model()

        class CustomUserChangeForm(UserChangeForm):

            class Meta(UserChangeForm.Meta):
                model = get_user_model()
                fields = ('email', 'first_name', 'last_name')
        ```
        - `get_user_model()`
            - 현재 프로젝트에서 활성화된 사용자 모델(active user model)을 반환
        - fields를 통해 접근 가능한 필드를 조정

- 회원가입
    - User를 CREATE
    ```python
    from .forms import CustomUserCreationForm, CustomUserChangeForm

    def signup(request):
        if requesst.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()          # UserCreationForm의 save 메서드는 user를 반환함
                auth_login(request, user)   # 회원가입 후 곧바로 로그인
                return redirect('articles:index')
        else:
            form = CustomUserCreationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/signup.html', context)
    ```
    - `UserCreationForm`
        - username과 password로 권한이 없는 새 user를 생성하는 ModelForm
        - 3개의 필드를 가짐
            1. username (from the user model)
            2. password1
            3. password2

- 회원탈퇴
    - User를 DELETE
    ```python
    def delete(request):
        request.user.delete()
        auth_logout(request)    # 탈퇴 후 세션 정보도 함께 지움
        return redirect('articles:index')
    ```
    - 탈퇴 후 로그아웃의 순서가 바뀌면 안됨
        - 먼저 로그아웃 해버리면 탈퇴에 필요한 정보 또한 없어짐

- 회원정보수정
    - User를 UPDATE
    ```python
    def update(request):
        if requesst.method == 'POST':
            form = CustomUserChangeForm(request.POST, instance=request.user)
            # form = CustomUserChangeForm(data=request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('articles:index')
        else:
            form = CustomUserChangeForm(instance=request.user)
        context = {
            'form': form,
        }
        return render(request, 'accounts/update.html', context)
    ```
    - `UserChangeForm`
        - 사용자의 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용되는 ModelForm
        - instance 인자로 기존 user 데이터 정보를 받는 구조 또한 동일함
        - 커스텀시 접근 가능한 필드를 조정하지 않으면 접근해서는 안 될 정보들(fields)까지 모두 수정이 가능해짐

- 비밀번호변경
    ```python
    from django.contrib.auth.forms import AuthenticationForm, PasswordChagneForm
    from django.contrib.auth import update_session_auth_hash

    def change_password(request):
        if request.method =='POST':
            form = PasswordChangeForm(request.user, request.POST)
            # form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('articles:index')
        else:
            form = PasswordChangeForm(request.user)
        context = {
            'form': form,
        }
        return render(request, 'accounts/change_password.html', context)
    ```
    - `PasswordChangeForm`
        - 사용자가 비밀번호를 변경할 수 있도록 하는 Form
        - 이전 비밀번호를 입력하여 비밀번호를 변경
        - 비밀번호 변경 form 주소는 `/accounts/password/`
            - 회원정보 수정 페이지에서 확인 가능
    - `update_session_auth_hash(request, user)`
        - 암호가 변경되어도 로그아웃 되지 않도록 새로운 password의 session data로 session을 업데이트

- `@login_required` decorator
    - `from django.contrib.auth.decorators import login_required`
    - 사용자가 로그인 되어 있으면 정상적으로 view 함수를 실행
    - 로그인 하지 않으면 setting.py의 LOGIN_URL 문자열 주소로 redirect
        - 기본 값은 `/accounts/login/`
    - create, delete, update에 적용
        - 로그인 상태에서만 글을 작성/수정/삭제 할 수 있도록 변경
    - 로그인 페이지로 리다이렉트 후 인증 성공 시 사용자가 redirect 되어야하는 경로가 next라는 쿼리 문자열 매개 변수에 저장됨
        - 해당 값을 처리할지 말지는 자유
        - `return redirect(request.GET.get('next') or 'articles:index')`
        - login 템플릿에서 form action이 작성되어 있으면 동작하지 않으므로 지워줌
    - `@require_POST`와 구조적 문제
        - 405(Method Not Allowed) status code 를 받게 됨
        - 로그인 성공 이후 GET method로 next 파라미터 주소에 리다이렉트 되기 때문
        - `if request.user.is_authenticated:`
            - POST method만 허용하는 delete 같은 함수는 내부에서 is_authenticated 속성 값을 사용해서 처리

- accounts의 view 함수에도 데코레이터 및 속성 값 적용