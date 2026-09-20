from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.conf import settings
import requests
from .models import ComparisonArticle, ContactMessage
from bikes.models import Bike


def send_telegram_notification(name, email, message):
    """Отправляет уведомление в Telegram о новом сообщении."""
    token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_CHAT_ID

    if not token or not chat_id:
        print('TELEGRAM ERROR: token or chat_id not set')
        return

    text = (
        f'💬 Новое сообщение на Old Rebel\n\n'
        f'👤 Имя: {name}\n'
        f'📧 Email: {email}\n\n'
        f'📝 Сообщение:\n{message}'
    )

    try:
        url = f'https://api.telegram.org/bot{token}/sendMessage'
        response = requests.post(url, data={'chat_id': chat_id, 'text': text}, timeout=10)
        if response.status_code != 200:
            print(f'TELEGRAM ERROR: {response.text}')
    except Exception as e:
        print(f'TELEGRAM ERROR: {e}')


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
    era = request.GET.get('era', 'all')
    bikes = Bike.objects.all().order_by('years')

    if era == 'fx':
        bikes = bikes.filter(code__in=['FX', 'FXB', 'FXR'])
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


def comparison_list(request):
    articles = ComparisonArticle.objects.all().order_by('order')
    breadcrumbs = [
        {'name': 'Сравнительные материалы', 'url': ''},
    ]
    return render(request, 'comparison_list.html', {
        'articles': articles,
        'breadcrumbs': breadcrumbs
    })


def comparison_detail(request, slug):
    article = get_object_or_404(ComparisonArticle, slug=slug)
    breadcrumbs = [
        {'name': 'Сравнительные материалы', 'url': '/comparison/'},
        {'name': article.title, 'url': ''},
    ]
    return render(request, 'comparison_detail.html', {
        'article': article,
        'breadcrumbs': breadcrumbs
    })


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


def sources(request):
    breadcrumbs = [
        {'name': 'Источники', 'url': ''},
    ]
    return render(request, 'sources.html', {'breadcrumbs': breadcrumbs})


def bike_detail(request, slug):
    bike = get_object_or_404(Bike, slug=slug)
    breadcrumbs = [
        {'name': 'Модели', 'url': '/models/'},
        {'name': bike.name, 'url': ''},
    ]
    return render(request, 'bikes/detail.html', {
        'bike': bike,
        'breadcrumbs': breadcrumbs
    })


def contact(request):
    breadcrumbs = [
        {'name': 'Контакты', 'url': ''},
    ]
    return render(request, 'contact.html', {'breadcrumbs': breadcrumbs})


def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Сохраняем в базу данных
        ContactMessage.objects.create(name=name, email=email, message=message)

        # Отправляем уведомление в Telegram
        send_telegram_notification(name, email, message)

        messages.success(request, 'Сообщение отправлено! Мы ответим вам в ближайшее время.')
        return redirect('contact')
    return redirect('contact')