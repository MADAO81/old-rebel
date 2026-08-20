from django.shortcuts import render
from bikes.models import Bike

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def history(request):
    return render(request, 'history.html')

def models_list(request):
    bikes = Bike.objects.all().order_by('years')
    return render(request, 'models.html', {'bikes': bikes})

def comparison(request):
    return render(request, 'comparison.html')

def soa(request):
    return render(request, 'soa.html')

def legal(request):
    return render(request, 'legal.html')