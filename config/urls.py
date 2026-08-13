from django.contrib import admin
from django.urls import path, include
from pages.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('bikes/', include('bikes.urls')),  # подключаем маршруты для мотоциклов
]