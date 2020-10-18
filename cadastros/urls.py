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
]
