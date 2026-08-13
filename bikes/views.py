from django.shortcuts import render, get_object_or_404
from .models import Bike

def bike_detail(request, slug):
    bike = get_object_or_404(Bike, slug=slug)
    return render(request, 'bike_detail.html', {'bike': bike})