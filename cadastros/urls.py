from django.urls import path
from .views import *

urlpatterns = [

    path('cadastrar/disciplina', DisciplinaCreate.as_view(),
         name="cadastrar-disciplina"),
    path('cadastrar/bloco', BlocoCreate.as_view(), name="cadastrar-bloco"),
    path('cadastrar/atividade', AtividadeCreate.as_view(),
         name="cadastrar-atividade"),

    path('editar/disciplina/<int:pk>/', DisciplinaUpdate.as_view(),
         name="editar-disciplina"),
    path('editar/bloco/<int:pk>/', BlocoUpdate.as_view(),
         name="editar-bloco"),
    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(),
         name="editar-atividade"),

    path('excluir/disciplina/<int:pk>/', DisciplinaDelete.as_view(),
         name="excluir-disciplina"),
    path('excluir/bloco/<int:pk>/', BlocoDelete.as_view(),
         name="excluir-bloco"),
    path('excluir/atividade/<int:pk>/', AtividadeDelete.as_view(),
         name="excluir-atividade"),

    path('listar/disciplinas/', DisciplinaList.as_view(),
         name="listar-disciplinas"),
    path('listar/blocos/', BlocoList.as_view(),
         name="listar-blocos"),
    path('listar/atividades/', AtividadeList.as_view(),
         name="listar-atividades"),
]
