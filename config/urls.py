from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages.views import index, about, history, models_list, comparison, soa, legal, bike_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('history/', history, name='history'),
    path('models/', models_list, name='models'),
    path('bikes/<slug:slug>/', bike_detail, name='bike_detail'),
    path('blog/', include('blog.urls')),
    path('comparison/', comparison, name='comparison'),
    path('soa/', soa, name='soa'),
    path('legal/', legal, name='legal'),
]

# Раздаём медиа-файлы (только в режиме разработки)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)