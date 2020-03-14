from django.contrib import admin
from .models import ingresso,evento,pessoa,inscricao,pessoaFisica

@admin.register(ingresso,evento,pessoa,inscricao,pessoaFisica)
class ingressoAdmin(admin.ModelAdmin):
    pass


# Register your models here.
