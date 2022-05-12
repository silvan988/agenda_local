from django.db import models
from django.utils import timezone

from categorias.models import Categoria
from django.contrib.auth.models import User


class Contato(models.Model):
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    #email = models.CharField(max_length=255, blank=True)
    email = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Usuário')
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/')

    def __str__(self):
        return self.nome

