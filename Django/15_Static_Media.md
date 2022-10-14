- Static files
    - 정적 파일
    - 파일 자체가 고정되어 있고, 서비스 중에도 추가되거나 변경되지 않고 고정 되어있음
        - 이미지, 자바 스크립트 또는 CSS
    - Media File
        - 미디어 파일
        - 사용자가 웹에서 업로드하는 정적 파일
    - `{% load static %}`
        - 특정 라이브러리, 패키지에 등록된 모든 템플릿 태그와 필터를 로드
        - STATIC_ROOT에 저장된 정적 파일에 연결해주는 static tag를 로드
    - settings
        - `STATIC_ROOT`
            - 프로젝트에서 사용하는 모든 정적 파일을 한곳에 모아 넣는 경로
            - `python manage.py collectstatic`을 통해 정적파일 수집
        - `STATICFILES_DIRS`
            - `app/static/` 외에 추가적인 정적 파일 경로 목록을 정의하는 리스트
            - `STATICFILES_DIRS = [BASE_DIR / 'static',]`
        - `STATIC_URL`
            - STATIC_ROOT에 있는 정적 파일을 참조 할 때 사용할 URL
            - 개발 단계에서는 실제 정적 파일들이 저장되어 있는 app/static/ 경로 및 STATICFILES_DIRS에 정의된 추가 경로들을탐색
            - 실제 파일이나 디렉토리가 아니며, URL로만 존재
            - `STATIC_URL = '/static/'`
    - 사용하기
        - 기본 경로에 있는 static file 가져오기
            - articles/static/article 경로에 이미지 파일 배치
            - `<img src="{% static 'articles/sample_img_1.png' %}" alt="sample-img-1">`
        - 추가 경로에 있는 static file 가져오기
            - STATICFILES_DIRS 작성
            - static/ 경로에 이미지 파일 배치
            - `<img src="{% static 'sample_img_2.png' %}" alt="sample-img-2">`

- Image Upload
    - ImageField
        - 이미지 업로드에 사용하는 모델 필드
        - FileField를 상속 받는 서브 클래스
        - settings
            - `MEDIA_ROOT`
                - 사용자가 업로드한 파일들을 보관할 디렉토리의 절대 경로
                - 데이터베이스에는 파일 경로만 저장됨
                - STATIC_ROOT와 다른 경로로 지정해야 함
                - `MEDIA_ROOT = BASE_DIR / 'media'`
            - `MEDIA_URL`
                - MEDIA_ROOT에서 제공되는 미디어 파일을 처리하는 URL
                - 업로드 된 파일의 주소(URL)을 만들어 주는 역할
                - STATIC_URL과 다른 경로로 지정해야 함
                - `MEDIA_URL = '/media/'`
        - urls
            - urlpatterns에 `+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`
                - `from django.conf import settings`
                - `from django.conf.urls.static import static`
    - CREATE
        - model
            - `image = models.ImageField(blank=True)`
                - blank
                    - Ture인 경우 필드를 비워 둘 수 있음
                    - 이때 ''(빈 문자열)이 저장됨
                    - 유효성 검사에서 사용됨(is_valid)
                    - [docs](https://docs.djangoproject.com/en/3.2/ref/models/fields/#blank)
                - null
                    - True인 경우 빈 값을 DB에 NULL로 저장
                    - CharField, TextField와 같은 문자열 기반 필드에서는 사용을 피해야 함
            - makemigrations 하기 전에 Pillow 라이브러리가 필요
                - `pip install Pillow`
                    - `pip freeze > requirements.txt` 잊지 말것
        - 템플릿
            - 파일 또는 이미지 업로드 시에는 form 태그에 enctype 속성 변경 필요
                - `enctype="aplication/x-www-form-urlencoded"`
                    - 기본 값
                    - 모든 문자 인코딩
                - `enctype="multipart/form-data"`
                    - 변경해야 하는값
                    - 파일/이미지 업로드시에반드시 사용해야 함
                    - 전송되는 데이터의 형식을 지정
                - `enctype="text/plain"`
                    - 설명 없음
        - views
            - 파일 및 이미지는 request의 POST 속성 값으로 넘어가지 않고 FILES 속성 값에 담겨 넘어감
                - `form = ArticleForm(request.POST, request.FILES)`
        - 같은 이름의 파일을 업로드하면 파일 이름 끝에 임의의 난수 값을 붙여 저장함
    - READ
        - 업로드 된 파일의 상대 URL은 url 속성을 통해 얻을 수 있음
            - `<img src="{{ article.image.url }}" alt="{{ article.image }}">`
            - 이때 이미지를 업로드하지 않은 게시물은 출력할 수 없으므로 `{% if article.image %}`를 통해 처리
    - UPDATE
        - 이미지는 텍스트처럼 일부만 수정 하는 것은 불가능
        - 새로운 사진으로 대체하는 방식을 사용
        - 템플릿
            - 마찬가지로 `enctype="multipart/form-data"`추가
        - views
            - 마찬가지로 `request.FILES`추가
    - `upload_to` argument
        1. 문자열 값이나 경로 지정 방법
            - ImageField에 `upload_to='images/'`를 추가하면 이미지는 MEDIA_ROOT 이후 경로가 추가됨
            - `upload_to='%Y/%m/%d/'`와 같이 time 모듈의 strftime() 형식도 포함될 수 있음
        2. 함수 호출 방법
            ```python
            def articles_image_path(instance, filename):
                return f'images/{instance.user.username}/{filename}'
            ```
            - `upload_to=articles_image_path`
            - 함수가 호출 되면서 2개의 인자를 받음
                - instance
                    - FileFiled가 정의된 모델의 인스턴스
                    - 데이터베이스에 저장되기 전이므로 PK 값이 없을 수 있음
                - filename
                    - 기존 파일 이름

- Image Resizing
    - django-imagekit
        - `pip install django-imangekit`
            - requirements.txt 저장
        - INSTALLED_APPS에 'imagekit' 추가
        - 이미지 처리를 위한 장고 앱
    1. 원본 이미지 저장 X
        - models
            ```python
            image = ProcessedImageField(
                blank=True,
                upload_to='thumbnails/',
                processors=[Thumbnail(200,300)],
                format='JPEG',
                options={'quality': 80},
            )
            ```
            - `from imagekit.processors import Thumbnail`
            - `from imagekit.models import ProcessedImageField`
            - [processors에 작성하는 여러 클래스](https://github.com/matthewwithanm/pilkit)
    2. 원본 이미지 저장 O
        - models
            ```python
            image = models.ImageField(blank=True)
            image_thumbnail = ImageSpecField(
                source='image',
                processors=[Thumbnail(200,300)],
                format='JPEG',
                options={'quality': 80},
            )
            ```
            - `from imagekit.processors import Thumbnail`
            - `from imagekit.models import ImageSpecField`
            - `<img src="{{ article.image_thumbnail.url }}" alt="{{ article.image_thumbnail }}">`
                - 썸네일이 사용되었을 때만 resizing한 이미지를 생성