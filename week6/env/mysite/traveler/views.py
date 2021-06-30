from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination, Welcome, Css


# Create your views here.

def index(request):

    dests = Destination.objects.all()
    welc = Welcome.objects.all()
    css = Css.objects.all()
    return render(request, 'index.html', {'dests': dests, 'welcome': welc, 'css': css})