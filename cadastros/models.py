from django.db import models
from django.contrib.auth.models import User

class Disciplina(models.Model):
    nome = models.CharField(max_length=150)
    nomeProfessor = models.CharField(
        max_length=150, verbose_name="Nome do Professor(a)")
    emailProfessor = models.CharField(
        max_length=150, verbose_name="E-mail do Professor(a)")
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return "{}\n{} ({})".format(self.nome, self.nomeProfessor, self.emailProfessor)


class Bloco(models.Model):
    titulo = models.CharField(max_length=150, verbose_name="Título")
    dataInicio = models.DateField(verbose_name="Data de ínicio")
    dataFinal = models.DateField(verbose_name="Data final")
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return "{} (Data de ínicio {}- Data Final {})".format(self.titulo, self.dataInicio, self.dataFinal)


class Atividade(models.Model):
    titulo = models.CharField(max_length=150, verbose_name="Título")
    dataEntrega = models.DateField(verbose_name="Data de entrega")
    STATUS_ATIVIDADE = [
        ('PENDENTE', 'Pendente'),
        ('INICIADO', 'Iniciado'),
        ('FINALIZADO', 'Finalizado')
    ]
    status = models.CharField(
        max_length=10, choices=STATUS_ATIVIDADE, default='PENDENTE')
    isAvaliativo = models.BooleanField(verbose_name="É avaliativo?")
    descricao = models.CharField(max_length=180, verbose_name="Descrição")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE,
                                   verbose_name="Disciplina")
    bloco_id = models.ForeignKey(Bloco, on_delete=models.CASCADE,
                                 verbose_name="Bloco")
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}\n{}\n{}\n{}\n{} ".format(self.titulo, self.disciplina, self.descricao, self.dataEntrega, self.isAvaliativo, self.status)
