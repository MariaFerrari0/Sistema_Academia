from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá, mundo! Este é o meu site de academia.")

def contato(request):
    return HttpResponse("Contato")

def sobre(request):
    return HttpResponse("Sobre")
# Create your views here.
