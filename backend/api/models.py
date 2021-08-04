from django.db import models
from django.conf import settings
from django.utils import timezone


class Company(models.Model):
    name = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=20)
    companyType = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Denuncia(models.Model):
    endereco = models.CharField(max_length=200)
    numero = models.CharField(max_length=5)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=80)
    descricao = models.CharField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.endereco


class Cadastro(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=30)
    senha = models.CharField(max_length=20)
    confirmacaoSenha = models.CharField(max_length=20)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email

class PontosDeColeta(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=50)
    materialColeta = models.CharField(max_length=50)
    tipoMaterial = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome

        