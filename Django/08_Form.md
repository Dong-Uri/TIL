- 유효성 검사 도구
    - 외부의 악의적 공격 및 데이터 손상에 대한 중요한 방어 수단
    - 단순화하고 자동화하는 기능 제공
        - 과중한 작업과 반복 코드를 줄여줌

- forms.py
    - Model Class 선언과 비슷
    - forms 라이브러리의 Form 클래스 상속을 통해 선언
    ```python
    from django import forms

    class ArticleForm(forms.Form):
        title = forms.CharField(max_length=10)
        content = forms.CharField()
    ```
    - TextFidld가 존재하지 않음
    - 어디든 작성해도 되지만 관행적으로 forms.py 파일 안에 작성

- new 변경
    ```python
    def new(request):
        form = ArticleForm()
        context = {
            'form': form,
        }
        return render(request, 'articles/new.html', context)
    ```
    ```html
    <form action="{% url 'articles:create' %}" method="POST">
        {% csrf_token %}
        {% form.as_p %}
        <input type="submit">
    </form>
    ```
    - input과 label 태그가 모두 렌더링 됨
    - 각 태그의 속성 값들도 자동으로 설정 됨
    - as_p()
        - 각 필드가 `<p>`태그로 감써져서 렌더링
    - as_ul()
        - 각 필드가 `<li>`태그로 감써져서 렌더링
        - `<ul>`태그는 직접 작성
    - as_p()
        - 각 필드가 `<tr>`태그로 감써져서 렌더링

- Form fields
    - 입력에 대한 유효성 검사 로직 처리
    - 템플릿에서 직접 사용됨
    - [목록](https://docs.djangoproject.com/ko/3.2/ref/forms/fields/)

- Widgets
    - HTML input 요소 렌더링(표현) 담당
    - 유효성 검증과 관계 없음
    - form fields에 할당 됨
    - [목록](https://docs.djangoproject.com/ko/3.2/ref/forms/widgets/#built-in-widgets)
    - textarea 위젯
        - `CharField(widget=forms.Textarea)`