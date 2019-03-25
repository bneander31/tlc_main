from django.shortcuts import render
from django.http import HttpResponse
from .models import Location

def index(request):
    locations = Location.objects.all()
    return render(request, 'pages/index.html', {'locations': locations})


def about(request):
    return render(request, 'pages/about.html')

