from django.shortcuts import render

# Create your views here.
from .models import *
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class DisciplinaCreate(CreateView):
    model = Disciplina
    fields = ['nome', 'nomeProfessor', 'emailProfessor']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')


class BlocoCreate(CreateView):
    model = Bloco
    fields = ['titulo', 'dataInicio', 'dataFinal']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')


class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['titulo', 'dataEntrega', 'status',
              'isAvaliativo', 'descricao', 'disciplina', 'bloco_id']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')


class DisciplinaUpdate(UpdateView):
    model = Disciplina
    fields = ['nome', 'nomeProfessor', 'emailProfessor']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')


class BlocoUpdate(UpdateView):
    model = Bloco
    fields = ['titulo', 'dataInicio', 'dataFinal']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')


class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['titulo', 'dataEntrega', 'status',
              'isAvaliativo', 'descricao', 'disciplina', 'bloco_id']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')
