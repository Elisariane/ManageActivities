from django.db import models

# Create your models here.


class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    senha = models.CharField(max_length=50)

    def __str__(self):
        return "{} ({})".format(self.nome, self.email)


class Disciplina(models.Model):
    nome = models.CharField(max_length=150)
    nomeProfessor = models.CharField(
        max_length=150, verbose_name="Nome do Professor(a)")
    emailProfessor = models.CharField(
        max_length=150, verbose_name="E-mail do Professor(a)")


class Atividade(models.Model):
    titulo = models.CharField(max_length=150, verbose_name="Título")
    dataEntrega = models.DateField(verbose_name="Data de entrega")
    PENDENTE = 'Pendente'
    INICIADO = 'Iniciado'
    FINALIZADO = 'Finalizado'

    STATUS_ATIVIDADE = [
        (PENDENTE, 'Pendente'),
        (INICIADO, 'Iniciado'),
        (FINALIZADO, 'Finalizado'),
    ]
    status = models.CharField(
        max_length=1,
        choices=STATUS_ATIVIDADE,
        default='Selecione',
    )

    isAvaliativo = models.BooleanField()
    descricao = models.CharField(max_length=180, verbose_name="Descrição")

    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)


class Bloco(models.Model):
    titulo = models.CharField(max_length=150, verbose_name="Título")
    dataInicio = models.DateField(verbose_name="Data de ínicio")
    dataFinal = models.DateField(verbose_name="Data final")

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
