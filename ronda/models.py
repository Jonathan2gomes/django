from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    cnh = models.CharField(max_length=30)
    data_nasc = models.DateField()

    def __str__(self):
        return self.nome


class Moto(models.Model):
    modelo = models.CharField(max_length=10)
    preco = models.FloatField(max_length=10)
    descricao = models.CharField(max_length=30)
    ano = models.CharField(max_length=10, default='2020')
    marca = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.modelo


class Venda(models.Model):
    nota_fiscal = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE)
