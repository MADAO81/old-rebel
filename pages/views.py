from django.shortcuts import render, get_object_or_404
from bikes.models import Bike

def index(request):
    breadcrumbs = [
        {'name': 'Главная', 'url': ''},
    ]
    return render(request, 'index.html', {'breadcrumbs': breadcrumbs})

def about(request):
    breadcrumbs = [
        {'name': 'О проекте', 'url': ''},
    ]
    return render(request, 'about.html', {'breadcrumbs': breadcrumbs})

def history(request):
    breadcrumbs = [
        {'name': 'История', 'url': ''},
    ]
    return render(request, 'history.html', {'breadcrumbs': breadcrumbs})

def models_list(request):
    bikes = Bike.objects.all().order_by('years')
    breadcrumbs = [
        {'name': 'Модельный ряд', 'url': ''},
    ]
    return render(request, 'models.html', {'bikes': bikes, 'breadcrumbs': breadcrumbs})

def comparison(request):
    breadcrumbs = [
        {'name': 'Сравнительные материалы', 'url': ''},
    ]
    return render(request, 'comparison.html', {'breadcrumbs': breadcrumbs})

def soa(request):
    breadcrumbs = [
        {'name': 'Сыны Анархии', 'url': ''},
    ]
    return render(request, 'soa.html', {'breadcrumbs': breadcrumbs})

def legal(request):
    breadcrumbs = [
        {'name': 'Юридическая информация', 'url': ''},
    ]
    return render(request, 'legal.html', {'breadcrumbs': breadcrumbs})

def bike_detail(request, slug):
    bike = get_object_or_404(Bike, slug=slug)
    breadcrumbs = [
        {'name': 'Модели', 'url': '/models/'},
        {'name': bike.name, 'url': ''},
    ]
    return render(request, 'bikes/bike_detail.html', {'bike': bike, 'breadcrumbs': breadcrumbs})