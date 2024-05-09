from django.db import models
from datetime import datetime
from veiculo.consts import OPCOES_CORES, OPCOES_COMBUSTIVEL, OPCOES_MARCAS

class Veiculo(models.Model):
    marca = models.SmallIntegerField(choices=OPCOES_MARCAS)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    cor = models.SmallIntegerField(choices=OPCOES_CORES)
    foto = models.ImageField(blank=True, null=True, upload_to='veiculo/fotos')
    combustivel = models.SmallIntegerField(choices=OPCOES_COMBUSTIVEL)

    def __str__(self):
        return '{0} - {1} ({2}/{3})'.format(
            self.get_marca_display(),
            self.modelo,
            self.ano,
            self.get_cor_display()
        )
    
    def get_nome_marca(self):
        for codigo, nome in OPCOES_MARCAS:
            if self.marca == codigo:
                return nome
        return None