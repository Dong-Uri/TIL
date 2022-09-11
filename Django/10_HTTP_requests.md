- new와 edit는 GET 요청에 대한 처리만 진행
- create와 update는 POST 요청에 대한 처리만 진행

- CREATE
    ```python
    def create(request):
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            if form.is_valid():
                article = form.save()
                return redirect('ariticles:detail', article.pk)
        else:
            form = ArticleForm()
        context = {
            'form': form,
        }
        return render(request, 'articles/create.html', context)
    ```
    - new의 view 함수와 url path 삭제

- UPDATE
    ```python
    def update(request, pk):
        article = Article.objects.get(pk=pk)
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('ariticles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            'form': form,
            'article': article,
        }
        return render(request, 'articles/update.html', context)
    ```
    - edit의 view 함수와 url path 삭제

- DELETE
    ```python
    def delete(request, pk):
        article = Article.objects.get(pk=pk)
        if request.method == 'POST':
            article.delete()
            return redirect('articles:index')
        return redirect('articles:detail', article.pk)
    ```
    - POST 요청에 대해서만 삭제 가능하도록

- View decorators
    - `from django.views.decorators.http import require_http_methods, require_POST, require_safe`
        - 요청 메서드를 기반으로 접근을 제한할 수 있음
        - 일치하지 않는 메서드 요청이라면 405 Method Not Allowed 반환
            - 요청 방법이 서버에게 전달 되었으나 사용 불가능한 상태
    - `@require_http_methods(['GET', 'POST'])`
        - 특정한 요청 method만 허용하도록 하는 데코레이터
        - create, update에 사용
    - `@require_POST`
        - POST 요청 method만 허용하도록 하는 데코레이터
        - delete에 사용
            - url로 delete 시도하면 405
    - `@require_safe`
        - require_GET이 있지만 require_safe를 사용하는 것을 권장
        - index, detail에 사용