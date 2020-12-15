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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastro da Disciplina'
        context['botao'] = 'Cadastrar'

        return context


class BlocoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Bloco
    fields = ['titulo', 'dataInicio', 'dataFinal']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-blocos')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastro do Bloco'
        context['botao'] = 'Cadastrar'
        return context


class AtividadeCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Atividade
    fields = ['titulo', 'dataEntrega', 'status',
              'isAvaliativo', 'descricao', 'disciplina', 'bloco_id']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividades')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastro da Atividade'
        context['botao'] = 'Cadastrar'
        return context


class DisciplinaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Disciplina
    fields = ['nome', 'nomeProfessor', 'emailProfessor']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-disciplinas')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Alteração de Disciplina'
        context['botao'] = 'Alterar'
        return context


class BlocoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Bloco
    fields = ['titulo', 'dataInicio', 'dataFinal']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-blocos')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Alteração de Bloco'
        context['botao'] = 'Alterar'
        return context


class AtividadeUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Atividade
    fields = ['titulo', 'dataEntrega', 'status',
              'isAvaliativo', 'descricao', 'disciplina', 'bloco_id']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividades')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Alteração da Atividade'
        context['botao'] = 'Alterar'
        return context


class DisciplinaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Disciplina
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-disciplinas')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Disciplina'
        return context


class BlocoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Bloco
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-blocos')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Bloco'
        return context


class AtividadeDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-atividades')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Atividade'
        return context


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
