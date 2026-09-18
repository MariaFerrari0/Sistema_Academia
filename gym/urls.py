from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('alunos/', views.lista_alunos, name='lista_alunos'),
    path('alunos/cadastrar/', views.cadastrar_aluno, name='cadastrar_aluno'),

    path('professores/', views.lista_professores, name='lista_professores'),
    path('professores/cadastrar/', views.cadastrar_professor, name='cadastrar_professor'),

    path('modalidades/', views.lista_modalidades, name='lista_modalidades'),
    path('modalidades/cadastrar/', views.cadastrar_modalidade, name='cadastrar_modalidade'),

    path('matriculas/', views.lista_matriculas, name='lista_matriculas'),
    path('matriculas/cadastrar/', views.cadastrar_matricula, name='cadastrar_matricula'),
]