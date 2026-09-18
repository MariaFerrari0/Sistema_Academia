from django.shortcuts import render


def home(request):
    return render(request, 'gym/home.html')


def lista_alunos(request):
    return render(request, 'gym/alunos/lista.html')


def cadastrar_aluno(request):
    return render(request, 'gym/alunos/cadastrar.html')


def lista_professores(request):
    return render(request, 'gym/professores/lista.html')


def cadastrar_professor(request):
    return render(request, 'gym/professores/cadastrar.html')


def lista_modalidades(request):
    return render(request, 'gym/modalidades/lista.html')


def cadastrar_modalidade(request):
    return render(request, 'gym/modalidades/cadastrar.html')


def lista_matriculas(request):
    return render(request, 'gym/matriculas/lista.html')


def cadastrar_matricula(request):
    return render(request, 'gym/matriculas/cadastrar.html')