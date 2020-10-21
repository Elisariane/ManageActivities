from django.shortcuts import render

# Create your views here.
from .models import *
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class DisciplinaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Disciplina
    fields = ['nome', 'nomeProfessor', 'emailProfessor']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-disciplinas')


class BlocoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Bloco
    fields = ['titulo', 'dataInicio', 'dataFinal']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-blocos')


class AtividadeCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Atividade
    fields = ['titulo', 'dataEntrega', 'status',
              'isAvaliativo', 'descricao', 'disciplina', 'bloco_id']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividades')


class DisciplinaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Disciplina
    fields = ['nome', 'nomeProfessor', 'emailProfessor']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-disciplinas')


class BlocoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Bloco
    fields = ['titulo', 'dataInicio', 'dataFinal']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-blocos')


class AtividadeUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Atividade
    fields = ['titulo', 'dataEntrega', 'status',
              'isAvaliativo', 'descricao', 'disciplina', 'bloco_id']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividades')


class DisciplinaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Disciplina
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-disciplinas')


class BlocoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Bloco
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-blocos')


class AtividadeDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-atividades')


class DisciplinaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Disciplina
    template_name = 'cadastros/listas/disciplinas.html'


class BlocoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Bloco
    template_name = 'cadastros/listas/blocos.html'


class AtividadeList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'cadastros/listas/atividades.html'
