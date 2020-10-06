from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Usuario)
admin.site.register(Bloco)
admin.site.register(Atividade)
admin.site.register(Disciplina)

