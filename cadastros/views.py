from django.shortcuts import render

# Create your views here.
from .models import *
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView


class DisciplinaCreate(CreateView):
    model = Disciplina
    fields = ['nome', 'nomeProfessor', 'emailProfessor']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-disciplinas')


class BlocoCreate(CreateView):
    model = Bloco
    fields = ['titulo', 'dataInicio', 'dataFinal']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-blocos')


class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['titulo', 'dataEntrega', 'status',
              'isAvaliativo', 'descricao', 'disciplina', 'bloco_id']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividades')


class DisciplinaUpdate(UpdateView):
    model = Disciplina
    fields = ['nome', 'nomeProfessor', 'emailProfessor']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-disciplinas')


class BlocoUpdate(UpdateView):
    model = Bloco
    fields = ['titulo', 'dataInicio', 'dataFinal']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-blocos')


class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['titulo', 'dataEntrega', 'status',
              'isAvaliativo', 'descricao', 'disciplina', 'bloco_id']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividades')


class DisciplinaDelete(DeleteView):
    model = Disciplina
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-disciplinas')


class BlocoDelete(DeleteView):
    model = Bloco
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-blocos')


class AtividadeDelete(DeleteView):
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-atividades')


class DisciplinaList(ListView):
    model = Disciplina
    template_name = 'cadastros/listas/disciplinas.html'


class BlocoList(ListView):
    model = Bloco
    template_name = 'cadastros/listas/blocos.html'


class AtividadeList(ListView):
    model = Atividade
    template_name = 'cadastros/listas/atividades.html'
