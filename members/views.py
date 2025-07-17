from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello World")
# Create your views here.

def index(request):
    return render(request, 'index.html')


def about(request): #done
    return render(request, 'about.html')


def contact(request): #done
    return render(request, 'contact.html')


def detail(request): #done
    return render(request, 'detail.html')


def feature(request): #done
    return render(request, 'feature.html')


def service(request): #done
    return render(request, 'service.html')


def team(request): #done
    return render(request, 'team.html')
