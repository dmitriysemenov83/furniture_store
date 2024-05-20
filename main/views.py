from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request) -> HttpResponse:
    categories = Categories.objects.all()
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели Home',
        'categories': categories
    }
    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    context = {
        'title': 'О нас',
        'content': 'О нас',
        'text_on_page': 'Добавить текст'
    }
    return render(request, 'main/about.html', context)
