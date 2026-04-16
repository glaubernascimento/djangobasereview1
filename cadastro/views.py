# cadastro\views.py

from django.shortcuts import get_object_or_404, redirect, render
from cadastro.forms import PessoaForm
from cadastro.models import Pessoa
from django.contrib.auth.decorators import login_required


def index(request):
    # Recebe todas as pessoas do banco de dados
    # pessoas = Pessoa.objects.all()

    # Recebe todas as pessoas em ordem alfabética do nome
    pessoas = Pessoa.objects.order_by('nome')

    # Total de cadastrados
    total = Pessoa.objects.count()

    # Dicionário que passa dados para o template
    context = {
        'pessoas': pessoas,
        'total': total,
    }
    return render(request, 'cadastro/index.html', context)


def contato(request):
    return render(request, 'cadastro/contato.html')


# Só pode ser acessado por um usuátio autenticado
@login_required
def adicionar(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PessoaForm()
    return render(request, 'cadastro/adicionar.html', {'form': form})



def detalhe(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    return render(request, 'cadastro/detalhe.html', {'pessoa': pessoa})

# Só pode ser acessado por um usuátio autenticado
@login_required
def editar(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('detalhe', id=id)
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'cadastro/editar.html', {'form': form, 'pessoa': pessoa})

# Só pode ser acessado por um usuátio autenticado
@login_required
def deletar(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('index')
    return render(request, 'cadastro/deletar.html', {'pessoa': pessoa})