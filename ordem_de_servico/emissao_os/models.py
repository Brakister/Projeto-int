# models.py

from django.db import models

class Loja(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)

    class Meta:
        app_label = 'emissao_os'

    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class OrdemServico(models.Model):
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    servicos = models.ManyToManyField(Servico)
    data_emissao = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Ordem de Serviço {self.pk} - {self.loja} - {self.data_emissao}"
