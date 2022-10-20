- Response JSON
    - JSON을 데이터 응답
        - 정렬된 json을 출력하려면 크롬 확장프로그램 JSON Viewer 설치 필요
        1. HTML 응답
            - 지금까지 Django로 응답 해오던 방식
        2. JsonResponse()를 사용한 JSON 응답
            ```python
            from django.http.response import JsonResponse

            def article_json_1(request):
                articles = Article.objects.all()
                articles_json = []

                for article in articles:
                    articles_json.append(
                        {
                            'id': article.pk,
                            'title': article.title,
                            'content': article.content,
                        }
                    )
                return JsonResponse(articles_json, safe=False)
            ```
            - `JsonResponse()`
                - JSON-encoded response를 만드는 클래스
                - safe parameter
                    - 기본 값은 True
                    - False로 설정 시 모든 타입의 객체를 serialization
        3. Django Serializer를 사용한 JSON 응답
            ```python
            from django.http.response import HttpResponse
            from django.core import serializers

            def article_json_2(request):
                articles = Article.objects.all()
                data = serializers.serialize('json', articles)
                return HttpResponse(data, content_type='application/json')
            ```
            - `HttpResponse()`를 활용한 JSON 응답
            - 모든 필드를 작성하지 않아도 됨
            - Serialization
                - 어떠한 언어나 환경에서도 나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정
                - 변환 포맷은 대표적으로 json, xml, yaml이 있으며 json이 가장 보편적으로 쓰임
                - `selialize()`
                    - Queryset 및 Model Instance와 같은 복잡한 데이터를 JSON, XML등의 유형으로 쉽게 변환 할 수 있는 Python 데이터 타입으로 만들어 줌
        4. Django REST framework를 사용한 JSON 응답
            - Django REST framework (DRF)
                - Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리
                - DRF의 serializer는 Form 및 ModleForm 클래스와 매우 유사하게 작동
                - [DRF](https://www.django-rest-framework.org/)
                    - `pip install djangorestframework`로 설치
                    - settings.py INSTALLED_APPS에 `'rest_framework',`추가
                    - serializers.py
                        ```python
                        from rest_framework import serializers
                        from .models import Article

                        class ArticleSerializer(serializers.ModelSerializer):

                            class Meta:
                                model = Article
                                fields = '__all__'
                        ```
                    - views.py
                        ```python
                        @api_view()
                        def article_json_3(request):
                            articles = Article.objects.all()
                            serializer = ArticleSerializer(articles, many=True)
                            return Response(serializer.data)
                        ```
                - DRF 전용 템플릿으로 응답함
            - 직접 requests 라이브러리를 사용하여 json 응답 받기
                - `pip install requests`
                ```python
                import requests
                from pprint import pprint

                response = requests.get('http://127.0.0.1:8000/api/v1/json-3/')
                result = response.json()

                pprint(result)
                ```