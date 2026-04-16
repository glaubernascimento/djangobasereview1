# cadastro\models.py

from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    idade = models.IntegerField()

    def __str__(self):
        return self.nome


class Telefone(models.Model):
    pessoa = models.ForeignKey(
        Pessoa, on_delete=models.CASCADE, related_name='telefones')
    numero = models.CharField(max_length=20)

    def __str__(self):
        return self.numero
