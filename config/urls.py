from django.contrib import admin
from django.urls import path, include
from pages.views import index, about, history, models_list, comparison, soa, legal, sitemap
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('history/', history, name='history'),
    path('models/', models_list, name='models'),
    path('bikes/', include('bikes.urls')),
    path('blog/', include('blog.urls')),
    path('comparison/', comparison, name='comparison'),
    path('soa/', soa, name='soa'),
    path('legal/', legal, name='legal'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('sitemap.xml', sitemap, name='sitemap'),
]