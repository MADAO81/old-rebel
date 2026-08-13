from django.urls import path
from .views import bike_detail

urlpatterns = [
    path('<slug:slug>/', bike_detail, name='bike_detail'),
]