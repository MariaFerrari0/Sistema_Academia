from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'gym/home.html', context={ 'name': 'Maria Luiza'})

# Create your views here.
