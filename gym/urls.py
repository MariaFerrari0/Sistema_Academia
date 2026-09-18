from django.urls import path
from gym.views import home, contato, sobre


#dominio/g
urlpatterns = [
    
    path('', home),
    path('contato/', contato),
    path('sobre/', sobre),
]
