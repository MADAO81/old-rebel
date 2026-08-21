from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from bikes.models import Bike
from django.template.loader import render_to_string


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
    # Получаем параметры фильтрации
    era = request.GET.get('era', 'all')

    # Базовая выборка всех моделей
    bikes = Bike.objects.all().order_by('years')

    # Применяем фильтры по эпохам
    if era == 'fx':
        # Прародители: только FX и FXR
        bikes = bikes.filter(code__iexact='FX') | bikes.filter(code__iexact='FXR')
    elif era == 'evolution':
        bikes = bikes.filter(
            years__icontains='1991') | bikes.filter(
            years__icontains='1992') | bikes.filter(
            years__icontains='1993') | bikes.filter(
            years__icontains='1994') | bikes.filter(
            years__icontains='1995') | bikes.filter(
            years__icontains='1996') | bikes.filter(
            years__icontains='1997') | bikes.filter(
            years__icontains='1998')
    elif era == 'twincam88':
        bikes = bikes.filter(
            years__icontains='1999') | bikes.filter(
            years__icontains='2000') | bikes.filter(
            years__icontains='2001') | bikes.filter(
            years__icontains='2002') | bikes.filter(
            years__icontains='2003') | bikes.filter(
            years__icontains='2004') | bikes.filter(
            years__icontains='2005') | bikes.filter(
            years__icontains='2006')
    elif era == 'twincam96':
        bikes = bikes.filter(
            years__icontains='2007') | bikes.filter(
            years__icontains='2008') | bikes.filter(
            years__icontains='2009') | bikes.filter(
            years__icontains='2010') | bikes.filter(
            years__icontains='2011') | bikes.filter(
            years__icontains='2012') | bikes.filter(
            years__icontains='2013') | bikes.filter(
            years__icontains='2014') | bikes.filter(
            years__icontains='2015') | bikes.filter(
            years__icontains='2016') | bikes.filter(
            years__icontains='2017')
    # Если era == 'all' — показываем все модели (без фильтра)

    # Пагинация: 12 моделей на страницу
    paginator = Paginator(bikes, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    breadcrumbs = [
        {'name': 'Модельный ряд', 'url': ''},
    ]

    return render(request, 'models.html', {
        'page_obj': page_obj,
        'bikes': page_obj.object_list,
        'breadcrumbs': breadcrumbs,
        'current_era': era,
    })


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

def sitemap(request):
    bikes = Bike.objects.all()
    sitemap_xml = render_to_string('sitemap.xml', {'bikes': bikes})
    return render(request, 'sitemap.xml', {'bikes': bikes}, content_type='application/xml')