from django.contrib import admin
from django.urls import path, include
from pages.views import index, about, history, models_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('history/', history, name='history'),
    path('models/', models_list, name='models'),
    path('bikes/', include('bikes.urls')),
    path('blog/', include('blog.urls')),
]