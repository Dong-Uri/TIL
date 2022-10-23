- Postman
    - API를 구축하고 사용하기 위한 플랫폼

- ModelSerializer
    - app에 serializer.py 생성
    ```python
    from rest_framework import serializers
    from .models import Article

    class ArticleListSerializer(serializers.ModelSerializer):

        class Meta:
            model = Article
            fields = ('id', 'title', 'content',)

    class ArticleSerializer(serializers.ModelSerializer):

        class Meta:
            model = Article
            fields = '__all__'
    ```
    - Serializer 클래스를 자동으로 만들 수 있는 shortcut을 제공
        1. Model 정보에 맞춰 자동으로 필드 생성
        2. serializer에 대한 유효성 검사기를 자동 생성
        3. `.create()`및 `.update()`의 간단한 기본 구현 포함    

- Article
    ```python
    from rest_framework.response import Response
    from rest_framework.decorators import api_view
    from rest_framework import status

    from .models import Article
    from .serializers import ArticleListSerializer, ArticleSerializer

    @api_view(['GET', 'POST'])
    def article_list(request):
        if request.method == 'GET':
            articles = Article.objects.all()
            serializer = ArticleList Serializer(articles, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = ArticleSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

    @api_view(['GET', 'DELETE', 'PUT'])
    def article_detail(request, article_pk):
        article = Article.objects.get(pk=article_pk)
        if request.method == 'GET':
            serializer = ArticleSerializer(article)
            return Response(serializer.data)

        elif request.method == 'DELETE':
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        elif request.method == 'PUT':
            serializer = ArticleSerializer(article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
    ```
    - `many=True`
        - 단일 객체 인스턴스 대신 QureySet 또는 객체 목록을 serialize함
    - DRF에서 api_view 데코레이터 작성 필수
        - view 함수가 응답해야 하는 HTTP 메서드 목록을 받음
        - 기본적으로 GET만 허용되며 다른 메서드 요청은 405 Method Not Allowed로 응답
    - POST 요청에 대한 데이터 생성이 성공했을 경우는 201 Created 상태 코드를 응답하고 실패 했을 경우는 400 Bad request를 응답
        - Postman에서는 POST로 Body의 form-data에 KEY와 VALUE 값을 보내서 응답 확인
    - `raiser_exception=True`
        - is_valid()에서 유효성 검사 오류가 있는 경우 ValidationError 예외를 발생시킴
        - DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리되며 기본적으로 HTTP 400 응답을 반환
    - DELETE 요청에 대한 데이터 삭제가 성공했을 경우는 204 No Content 상태 코드 응답
    - PUT 요청에 대한 데이터 수정이 성공했을 경우는 200 OK 상태 코드 응답

- Comment
    - serializers
        ```python
        class CommentSerializer(serializers.ModelSerializer):

            class Meta:
                model = Comment
                fields = '__all__'
                read_only_fields = ('article',)
        ```
        - read_only_fields를 사용해 외래 키 필드를 읽기 전용 필드로 설정
            - 해당 필드를 유효성 검사에서 제외시키고 데이터 조회 시에는 출력
    - views
        ```python
        @api_view(['GET'])
        def comment_list(request):
            comments = Comment.objects.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
        
        @api_view(['GET', 'DELETE', 'PUT'])
        def comment_detail(request, comment_pk):
            comments = Comment.objects.get(pk=comment_pk)
            if request.method == 'GET':
                serializer = CommentSerializer(comments)
                return Response(serializer.data)

            elif request.method == 'DELETE':
                comment.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

            elif request.method == 'PUT':
                serializer = CommentSerializer(comment, data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data)

        @api_view(['POST'])
        def comment_create(request, article_pk):
            article = Article.objects.get(pk=article_pk)
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(article=article)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        ```
        - Article과 달리 같은 serializer 사용
        - save()는 Serializer 인스턴스를 저장하는 과정에서 추가적인 데이터를 받을 수 있음
            - article_pk에 해당하는 article 객체를 추가적인 데이터로 넘겨 저장
    - 역참조 데이터 조회
        - 특정 게시글에 작성된 댓글 목록 출력
            - 기본 필드 override
            1. PrimaryKeyRelatedField()
                - `comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)`
                - models.py에서 related_name을 통해 이름 변경 가능
            2. Nested relationships
                - `comment_set = CommentSerializer(many=True, read_only=True)`
                - 모델 관계 상으로 참조 된 대상은 참조하는 대상의 표현에 포함되거나 중첩(nested)될 수 있음
                - 이러한 중첩된 관계는 serializers를 필드로 사용하여 표현 할 수 있음
                - 두 클래스의 상/하 위치를 변경해야 함 
        - 특정 게시글에 작성된 댓글의 개수 출력
            - 새로운 필드 추가
                - `comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)`
                - source
                    - 필드를 채우는 데 사용할 속성의 이름
                    - 점 표기법(dotted notation)을 사용하여 속성을 탐색 할 수 있음
        - 특정 필드를 override 혹은 추가한 경우 read_only_fields가 동작하지 않음

- shorcuts functions
    - django.shortcuts 패키지에서 여러 함수와 클래스를 제공
        - render(), redirect(), get_object_or_404(), get_list_or_404()
        - [docs](http://docs.djangoproject.com/en/3.2/topics/http/shortcuts/)
    - `get_object_or_404()`
        - 모델 manager objects에서 get()을 호출하지만 해당 객체가 없을 땐 기존 DoesNotExist 예외 대신 Http404를 raise함
        - `Article.objects.get(pk=article_pk)`를 `get_object_or_404(Article, pk=article_pk)`로 변경
        - comment도 마찬가지
    - `get_list_or_404()`
        - 모델 manager objects에서 filter()의 결과를 반환하고 해당 객체 목록이 없을 땐 Http404를 raise함
        - `Article.objects.all()`를 `get_list_or_404(Article)`로 변경
        - comments도 마찬가지
    - 존재하지 않는 게시글 조회 시 이전에는 500 상태코드를 응답했지만 현재는 404 상태코드를 응답