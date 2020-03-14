from django.db import models
from django.contrib.auth.models import User

class pessoaFisica(models.Model):
    cpf=models.CharField('CPF',max_length=14, blank=True, null=True)
    def __str__(self):
        return self.cpf

class pessoa(pessoaFisica):
    nome = models.CharField('Nome', max_length=128, blank=True, null=True)
    email = models.CharField('Email', max_length=128, blank=True, null=True)

    def __str__(self):
        return self.nome

class evento(models.Model):
    nome = models.CharField('Nome', max_length=128, blank=True, null=True)
    sigla = models.CharField('Sigla', max_length=128, blank=True, null=True)
    data_inicio = models.DateField('Data de inicio', blank=True, null=True)
    realizador = models.ForeignKey(pessoa, on_delete=models.CASCADE, blank=True, null=True)
    descricao = models.TextField('Descrição', max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.nome

class ingresso(models.Model):
     descricao = models.CharField('Nome', max_length=128)
     valor= models.FloatField(null=True)
     eventos = models.ForeignKey(evento, on_delete=models.CASCADE, blank=True, null=True)
     def __str__(self):
        return self.descricao

class inscricao(models.Model):
    pessoas = models.ForeignKey(pessoa, on_delete=models.CASCADE, blank=True, null=True)
    eventos = models.ForeignKey(evento, on_delete=models.CASCADE, blank=True, null=True)
    ingressos = models.ForeignKey(ingresso, on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        verbose_name='Inscrição'
        verbose_name_plural='Inscrições'

# Create your models here.
