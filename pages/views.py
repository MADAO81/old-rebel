from django.shortcuts import render
from bikes.models import Bike

def index(request):
    bikes = Bike.objects.all().order_by('years')
    return render(request, 'index.html', {'bikes': bikes})