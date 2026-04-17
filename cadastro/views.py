# cadastro\views.py

from django.shortcuts import get_object_or_404, redirect, render
from cadastro.forms import PessoaForm, TelefoneFormSet
from cadastro.models import Pessoa
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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


@login_required
def adicionar(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        # instance=Pessoa() é necessário para o formset saber o pai
        formset = TelefoneFormSet(request.POST, instance=Pessoa())

        if form.is_valid() and formset.is_valid():
            pessoa = form.save()             # salva e obtém o id
            formset.instance = pessoa        # vincula os telefones à pessoa salva
            formset.save()
            messages.success(request, 'Pessoa adicionada com sucesso!')
            return redirect('index')
    else:
        form = PessoaForm()
        formset = TelefoneFormSet(instance=Pessoa())

    return render(request, 'cadastro/adicionar.html', {
        'form': form,
        'formset': formset,
    })


def detalhe(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    return render(request, 'cadastro/detalhe.html', {'pessoa': pessoa})


@login_required
def editar(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)

    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        formset = TelefoneFormSet(request.POST, instance=pessoa)

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.success(request, f'{pessoa.nome} atualizada com sucesso!')
            return redirect('detalhe', id=id)
    else:
        form = PessoaForm(instance=pessoa)
        formset = TelefoneFormSet(instance=pessoa)  # já carrega os telefones existentes

    return render(request, 'cadastro/editar.html', {
        'form': form,
        'formset': formset,
        'pessoa': pessoa,
    })


@login_required
def deletar(request, id):
    # Só pode ser acessado por um usuátio autenticado
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        pessoa.delete()
        messages.success(request, 'Pessoa apagada com sucesso!')
        return redirect('index')        
    return render(request, 'cadastro/deletar.html', {'pessoa': pessoa})
