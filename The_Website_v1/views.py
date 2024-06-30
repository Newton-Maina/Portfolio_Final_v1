from django.shortcuts import render
from .models import Service

# Create your views here.
def index(request):
    return render(request, 'index.html',{'navbar': 'home'})

def about(request):
    return render(request, 'about.html',{'navbar': 'about'})

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html',{'navbar': 'services', 'services': services})

def portfolio(request):
    return render(request, 'portfolio.html',{'navbar': 'portfolio'})

def contact(request):
    return render(request, 'contact.html',{'navbar': 'contact'})
