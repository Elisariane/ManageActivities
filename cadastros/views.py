from django.shortcuts import render
from django.shortcuts import get_object_or_404

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

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

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

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

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

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

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
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Disciplina, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

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

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Bloco, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

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
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Bloco, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

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

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Disciplina, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Disciplina'
        return context


class BlocoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Bloco
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-blocos')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Bloco, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Bloco'
        return context


class AtividadeDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-atividades')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Atividade, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object
        
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Atividade'
        return context


class DisciplinaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Disciplina
    template_name = 'cadastros/listas/disciplinas.html'
    def get_queryset(self):
        self.object_list = Disciplina.objects.filter(usuario=self.request.user)
        return self.object_list


class BlocoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Bloco
    template_name = 'cadastros/listas/blocos.html'
    def get_queryset(self):
        self.object_list = Bloco.objects.filter(usuario=self.request.user)
        return self.object_list

class AtividadeList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'cadastros/listas/atividades.html'
    def get_queryset(self):
        self.object_list = Atividade.objects.filter(usuario=self.request.user)
        return self.object_list