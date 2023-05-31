from django.db import models


class Cliente(models.Model):
    nome_completo = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    data_registro = models.DateField(auto_now_add=True)


class Contato(models.Model):
    nome_completo = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    data_registro = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey(
        Cliente, related_name="contatos", on_delete=models.CASCADE
    )
