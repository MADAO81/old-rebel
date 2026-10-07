from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
import requests
from .models import ComparisonArticle, ContactMessage, CookieConsent
from bikes.models import Bike


def get_client_ip(request):
    """Возвращает IP клиента, учитывая прокси."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


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

    # Связанные: все остальные сравнения (до 4 штук)
    other_articles = ComparisonArticle.objects.exclude(slug=slug).order_by('order')[:4]
    related = [
        {
            'title': a.title.upper(),
            'subtitle': a.preview[:80] + ('...' if len(a.preview) > 80 else ''),
            'url': f'/comparison/{a.slug}/',
        }
        for a in other_articles
    ]

    return render(request, 'comparison_detail.html', {
        'article': article,
        'breadcrumbs': breadcrumbs,
        'related_articles': related,
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


def privacy(request):
    breadcrumbs = [
        {'name': 'Политика конфиденциальности', 'url': ''},
    ]
    return render(request, 'privacy.html', {'breadcrumbs': breadcrumbs})


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

    # Связанные: потомок + 3 другие модели
    related = []

    # 1. Потомок (если есть)
    if bike.previous_model:
        related.append({
            'title': bike.previous_model.name.upper(),
            'subtitle': f"{bike.previous_model.years} • {bike.previous_model.code}",
            'url': f'/bikes/{bike.previous_model.slug}/',
        })

    # 2. Другие модели — исключаем текущую и уже добавленного потомка
    exclude_slugs = [bike.slug]
    if bike.previous_model:
        exclude_slugs.append(bike.previous_model.slug)

    other_bikes = Bike.objects.exclude(slug__in=exclude_slugs).order_by('years')

    # Ищем модели с похожим кодом (например, FXD → FXDX → FXDXT)
    code_prefix = bike.code[:3]  # первые 3 символа кода
    similar = [b for b in other_bikes if b.code.startswith(code_prefix)][:3]

    # Если похожих мало — добираем по годам
    if len(similar) < 3:
        for b in other_bikes:
            if b not in similar:
                similar.append(b)
            if len(similar) >= 3:
                break

    for b in similar[:3]:
        related.append({
            'title': b.name.upper(),
            'subtitle': f"{b.years} • {b.code}",
            'url': f'/bikes/{b.slug}/',
        })

    return render(request, 'bikes/detail.html', {
        'bike': bike,
        'breadcrumbs': breadcrumbs,
        'related_articles': related,
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
        consent = request.POST.get('consent')

        # Проверка согласия на обработку ПДн
        if not consent:
            messages.error(request, 'Необходимо согласие на обработку персональных данных.')
            return redirect('contact')

        # Сохраняем в базу данных
        ContactMessage.objects.create(name=name, email=email, message=message)

        # Отправляем уведомление в Telegram
        send_telegram_notification(name, email, message)

        messages.success(request, 'Сообщение отправлено! Мы ответим вам в ближайшее время.')
        return redirect('contact')
    return redirect('contact')


@require_POST
def cookie_consent_submit(request):
    """Сохраняет выбор пользователя по cookie."""
    consent = request.POST.get('consent') == 'accepted'
    ip = get_client_ip(request)
    ua = request.META.get('HTTP_USER_AGENT', '')

    CookieConsent.objects.create(
        ip_address=ip,
        user_agent=ua,
        consent_given=consent,
    )

    response = JsonResponse({'status': 'ok', 'consent': consent})
    # Cookie на 1 год
    response.set_cookie(
        'cookie_consent',
        'accepted' if consent else 'rejected',
        max_age=60 * 60 * 24 * 365,
        samesite='Lax',
    )
    return response


# === СЫНЫ АНАРХИИ: СТАТЬИ О ГЕРОЯХ ===

def soa_jax(request):
    breadcrumbs = [
        {'name': 'Сыны Анархии', 'url': '/soa/'},
        {'name': 'Джекс Теллер', 'url': ''},
    ]
    related = [
        {'title': 'КЛЭЙ МОРРОУ', 'subtitle': '2008 Dyna Super Glide', 'url': '/soa/clay-morrow/'},
        {'title': 'ОППИ УИНСТОН', 'subtitle': '2001 Dyna Super Glide Sport', 'url': '/soa/opie-winston/'},
        {'title': 'ТИГ ТРЕЙГЕР', 'subtitle': '2006 FXDBI Dyna Street Bob', 'url': '/soa/tig-trager/'},
    ]
    return render(request, 'soa_heroes/jax-teller.html', {'breadcrumbs': breadcrumbs, 'related_articles': related})


def soa_clay(request):
    breadcrumbs = [
        {'name': 'Сыны Анархии', 'url': '/soa/'},
        {'name': 'Клэй Морроу', 'url': ''},
    ]
    related = [
        {'title': 'ДЖЕКС ТЕЛЛЕР', 'subtitle': '2003 FXDX Dyna Super Glide Sport', 'url': '/soa/jax-teller/'},
        {'title': 'ТИГ ТРЕЙГЕР', 'subtitle': '2006 FXDBI Dyna Street Bob', 'url': '/soa/tig-trager/'},
        {'title': 'ОППИ УИНСТОН', 'subtitle': '2001 Dyna Super Glide Sport', 'url': '/soa/opie-winston/'},
    ]
    return render(request, 'soa_heroes/clay-morrow.html', {'breadcrumbs': breadcrumbs, 'related_articles': related})


def soa_tig(request):
    breadcrumbs = [
        {'name': 'Сыны Анархии', 'url': '/soa/'},
        {'name': 'Тиг Трейгер', 'url': ''},
    ]
    related = [
        {'title': 'ДЖЕКС ТЕЛЛЕР', 'subtitle': '2003 FXDX Dyna Super Glide Sport', 'url': '/soa/jax-teller/'},
        {'title': 'ЧИБС ТЕЛФОРД', 'subtitle': '2006 FXDBI Dyna Street Bob', 'url': '/soa/chibs-telford/'},
        {'title': 'ОППИ УИНСТОН', 'subtitle': '2001 Dyna Super Glide Sport', 'url': '/soa/opie-winston/'},
    ]
    return render(request, 'soa_heroes/tig-trager.html', {'breadcrumbs': breadcrumbs, 'related_articles': related})


def soa_chibs(request):
    breadcrumbs = [
        {'name': 'Сыны Анархии', 'url': '/soa/'},
        {'name': 'Чибс Телфорд', 'url': ''},
    ]
    related = [
        {'title': 'ТИГ ТРЕЙГЕР', 'subtitle': '2006 FXDBI Dyna Street Bob', 'url': '/soa/tig-trager/'},
        {'title': 'ДЖЕКС ТЕЛЛЕР', 'subtitle': '2003 FXDX Dyna Super Glide Sport', 'url': '/soa/jax-teller/'},
        {'title': 'ШУСТРЫЙ', 'subtitle': '2007 Dyna Street Bob (Twin Cam 110)', 'url': '/soa/juice-ortiz/'},
    ]
    return render(request, 'soa_heroes/chibs-telford.html', {'breadcrumbs': breadcrumbs, 'related_articles': related})


def soa_juice(request):
    breadcrumbs = [
        {'name': 'Сыны Анархии', 'url': '/soa/'},
        {'name': 'Шустрый', 'url': ''},
    ]
    related = [
        {'title': 'ЧИБС ТЕЛФОРД', 'subtitle': '2006 FXDBI Dyna Street Bob', 'url': '/soa/chibs-telford/'},
        {'title': 'ХЭППИ ЛОУМЕН', 'subtitle': '2011 Dyna Street Bob', 'url': '/soa/happy-lowman/'},
        {'title': 'ДЖЕКС ТЕЛЛЕР', 'subtitle': '2003 FXDX Dyna Super Glide Sport', 'url': '/soa/jax-teller/'},
    ]
    return render(request, 'soa_heroes/juice-ortiz.html', {'breadcrumbs': breadcrumbs, 'related_articles': related})


def soa_happy(request):
    breadcrumbs = [
        {'name': 'Сыны Анархии', 'url': '/soa/'},
        {'name': 'Хэппи Лоумен', 'url': ''},
    ]
    related = [
        {'title': 'ТИГ ТРЕЙГЕР', 'subtitle': '2006 FXDBI Dyna Street Bob', 'url': '/soa/tig-trager/'},
        {'title': 'ДЖЕКС ТЕЛЛЕР', 'subtitle': '2003 FXDX Dyna Super Glide Sport', 'url': '/soa/jax-teller/'},
        {'title': 'ШУСТРЫЙ', 'subtitle': '2007 Dyna Street Bob (Twin Cam 110)', 'url': '/soa/juice-ortiz/'},
    ]
    return render(request, 'soa_heroes/happy-lowman.html', {'breadcrumbs': breadcrumbs, 'related_articles': related})


def soa_opie(request):
    breadcrumbs = [
        {'name': 'Сыны Анархии', 'url': '/soa/'},
        {'name': 'Оппи Уинстон', 'url': ''},
    ]
    related = [
        {'title': 'ДЖЕКС ТЕЛЛЕР', 'subtitle': '2003 FXDX Dyna Super Glide Sport', 'url': '/soa/jax-teller/'},
        {'title': 'КЛЭЙ МОРРОУ', 'subtitle': '2008 Dyna Super Glide', 'url': '/soa/clay-morrow/'},
        {'title': 'ТИГ ТРЕЙГЕР', 'subtitle': '2006 FXDBI Dyna Street Bob', 'url': '/soa/tig-trager/'},
    ]
    return render(request, 'soa_heroes/opie-winston.html', {'breadcrumbs': breadcrumbs, 'related_articles': related})


# === SITEMAP ===

def sitemap_view(request):
    bikes = Bike.objects.all()
    xml = render_to_string('sitemap.xml', {'bikes': bikes})
    return HttpResponse(xml, content_type='application/xml')
