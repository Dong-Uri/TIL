from django.urls import path
# 명시적 상대경로
from . import views

# 당장 path를 쓰지 않더라도 urlpatterns는 작성해야 함
app_name = 'pages'
urlpatterns = [
    path('index/', views.index, name='index'),
]
