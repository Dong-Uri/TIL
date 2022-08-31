import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')


def greeting(request):
    foods = ['apple', 'banana', 'coconut',]
    info = {
        'name': 'Alice',
    }
    context = {
        'info': info,
        'foods': foods,
    }
    return render(request, 'articles/greeting.html', context)


def dinner(request):
    foods = ['apple', 'banana', 'coconut',]
    pick = random.choice(foods)
    context = {
        'pick': pick,
        'foods': foods,
    }
    return render(request, 'articles/dinner.html', context)


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    # throw에서 보낸 데이터를 찾아서 저장
    # print(request)
    # print(type(request))
    # print(request.GET)
    # print(request.GET.get('message'))
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'articles/catch.html', context)


def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'articles/hello.html', context)

