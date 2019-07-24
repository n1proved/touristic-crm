from django.shortcuts import render
from .models import Tourist, Hotel, Excursion

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_tourists=Tourist.objects.all().count()
    num_hotels=Hotel.objects.all().count()
    # Доступные книги (статус = 'a')
    num_excurs=Excursion.objects.all().count()

    
    # Отрисовка HTML-шаблона index.html с данными внутри 
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_tourists':num_tourists,'num_hotels':num_hotels,'num_excurs':num_excurs},
    )

# Create your views here.
