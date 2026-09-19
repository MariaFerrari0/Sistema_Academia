from django.shortcuts import render, redirect

from .persistencia.arquivo_alunos import ArquivoAlunos


arquivo_alunos = ArquivoAlunos()


def home(request):
    return render(request, 'gym/home.html')


def lista_alunos(request):
    alunos = arquivo_alunos.listar()

    return render(
        request,
        'gym/alunos/lista.html',
        {'alunos': alunos}
    )


def cadastrar_aluno(request):
    if request.method == 'POST':
        peso = float(request.POST.get('peso'))
        altura = float(request.POST.get('altura'))

        if altura > 3:
            altura = altura / 100

        aluno = {
            'codigo': request.POST.get('codigo'),
            'nome': request.POST.get('nome'),
            'data_nascimento': request.POST.get('data_nascimento'),
            'peso': peso,
            'altura': altura
        }

        arquivo_alunos.inserir(aluno)

        return redirect('lista_alunos')

    return render(request, 'gym/alunos/cadastrar.html')


def editar_aluno(request, codigo):
    aluno = arquivo_alunos.buscar(codigo)

    if aluno is None:
        return redirect('lista_alunos')

    if request.method == 'POST':
        peso = float(request.POST.get('peso'))
        altura = float(request.POST.get('altura'))

        if altura > 3:
            altura = altura / 100

        aluno_atualizado = {
            'codigo': codigo,
            'nome': request.POST.get('nome'),
            'data_nascimento': request.POST.get('data_nascimento'),
            'peso': peso,
            'altura': altura
        }

        arquivo_alunos.atualizar(aluno_atualizado)

        return redirect('lista_alunos')

    return render(
        request,
        'gym/alunos/cadastrar.html',
        {
            'aluno': aluno,
            'editar': True
        }
    )
def excluir_aluno(request, codigo):
    arquivo_alunos.excluir(codigo)

    return redirect('lista_alunos')


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