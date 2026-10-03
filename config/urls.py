from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from pages.views import (
    index, about, history, models_list, comparison_list, comparison_detail,
    soa, legal, sources, bike_detail, contact, contact_submit,
    soa_jax, soa_clay, soa_tig, soa_chibs, soa_juice, soa_happy, soa_opie,
    sitemap_view, privacy, cookie_consent_submit,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('history/', history, name='history'),
    path('models/', models_list, name='models'),
    path('bikes/<slug:slug>/', bike_detail, name='bike_detail'),
    path('blog/', include('blog.urls')),
    path('comparison/', comparison_list, name='comparison_list'),
    path('comparison/<slug:slug>/', comparison_detail, name='comparison_detail'),
    path('soa/', soa, name='soa'),

    # Сыны Анархии — статьи о героях
    path('soa/jax-teller/', soa_jax, name='soa_jax'),
    path('soa/clay-morrow/', soa_clay, name='soa_clay'),
    path('soa/tig-trager/', soa_tig, name='soa_tig'),
    path('soa/chibs-telford/', soa_chibs, name='soa_chibs'),
    path('soa/juice-ortiz/', soa_juice, name='soa_juice'),
    path('soa/happy-lowman/', soa_happy, name='soa_happy'),
    path('soa/opie-winston/', soa_opie, name='soa_opie'),

    path('legal/', legal, name='legal'),
    path('privacy/', privacy, name='privacy'),
    path('cookie-consent/', cookie_consent_submit, name='cookie_consent_submit'),
    path('sources/', sources, name='sources'),
    path('contact/', contact, name='contact'),
    path('contact/submit/', contact_submit, name='contact_submit'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('sitemap.xml', sitemap_view, name='sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)