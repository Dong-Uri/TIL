- forms.py
    - Model을 통해 Form Class를 만들 수 있는 helper class
    - forms 라이브러리에서 파생된 ModelForm 클래스 상속
    - 정의한 ModelForm 클래스 안에 Meta 클래스를 선언
        - ModelForm의 정보를 작성하는 곳
    ```python
    from django import forms
    from .models import Article

    class ArticleForm(forms.ModelForm):

        class Meta:
            model = Article
            fields = '__all__'
    ```
    - fields 속성에 `'__all__'`을 사용하여 모델의 모든 필드를 포함
    - fields 대신 exclude 속성을 사용하여 포함하지 않을 필드를 지정할 수 있음
        - 둘다 지정할 때는 튜플 이용

- CREATE
    ```python
    def create(request):
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('ariticles:detail', article.pk)
        # print(f'에러: {form.errors}')
        context = {
            'form': form,
        }
        return render(request, 'articles/new.html', context)
    ```
    - 유효성 검사를 통과하면 데이터 저장 후 상세 페이지로 리다이렉트
    - 통과하지 못하면 작성 페이지로 리다이렉트
    - errors 속성
        - 유효성 검증을 실패한 원인이 딕셔너리 형태로 저장됨

- UPDATE
    ```python
    def edit(request, pk):
        article = Article.objects.get(pk=pk)
        form = ArticleForm(instance=article)
        context = {
            'article': article,
            'form': form,
        }
        return render(request, 'articles/edit.html', context)
    ```
    ```python
    def update(request, pk):
        article = Article.objects.get(pk=pk)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('ariticles:detail', article.pk)
        context = {
            'form': form,
            'article': article,
        }
        return render(request, 'articles/edit.html', context)
    ```
    - `save()`
        - 키워드 인자 instance 여부를 통해 행성할 지, 수정할 지를 결정
            - 제공되지 않는 경우 새 인스턴스를 만듦 (CREATE)
            - 제공되는 경우 인스턴스를 수정 (UPDATE)

- Form과 ModelForm
    - Form
        - 입력 데이터가 DB 저장에 사용되지 않거나 일부 데이터만 사용될 때 사용
        - 로그인의 경우 사용자의 데이터를 받아 인증 과정에서만 사용하고 별도로 DB에 저장하지 않음
    - ModelForm
        - 입력 받은 것을 그대로 DB 필드에 맞춰 저장할 때 사용
        - 데이터의 유효성 검사가 끝나면 어떤 레코드에 맵핑할지 알기 때문에 곧바로 save() 호출 가능

- Widgets
    ```python
    class ArticleForm(forms.ModelForm):
        title = forms.CharField(
            label='제목',
            widget=forms.TextInput(
                attrs={
                    'class': 'my-title',
                    'placeholder': 'Enter the title',
                    'maxlength': 10,
                }
            ),
        )
        content = forms.CharField(
            label='내용',
            widget=forms.Textarea(
                attrs={
                    'class': 'my-content',
                    'placeholder': 'Enter the content',
                    'rows': 5,
                    'cols': 50,
                }
            ),
            error_messages={
                'required': 'Please enter your content',
            },
        )

        class Meta:
            model = Article
            fields = '__all__'
    ```
    - widget 내의 maxlength는 input 태그에서 입력을 못하게 함
        - 데이터베이스와 연관된 것은 아님
    - 사실은 나중에 거의 vue로 넘어갈 일들이긴 함