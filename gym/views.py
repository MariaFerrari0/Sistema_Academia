from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'gym/home.html', context={ 'name': 'Maria Luiza'})


def contato(request):
    return HttpResponse("Contato")

def sobre(request):
    return HttpResponse("Sobre")
# Create your views here.
