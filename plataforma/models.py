# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from simple_history.models import HistoricalRecords

from common.models import BaseModel, LogicDeletable
from plataforma.constants import NODO_TAMANHO_IMAGEM_LISTAGEM_LARGURA, NODO_TAMANHO_IMAGEM_LISTAGEM_ALTURA
from plataforma.constants import NODOS_TAMANHO_IMAGEM_LISTAGEM_LARGURA, NODOS_TAMANHO_IMAGEM_LISTAGEM_ALTURA
from plataforma.constants import OBJETO_TAMANHO_IMAGEM_LISTAGEM_LARGURA, OBJETO_TAMANHO_IMAGEM_LISTAGEM_ALTURA


class BaseContatoModel(models.Model):

    contato_facebook = models.URLField(u"Facebook", null=True, blank=True)
    contato_whatsapp = models.URLField(u"WhatsApp", null=True, blank=True)
    contato_zoom = models.URLField(u"Zoom", null=True, blank=True)

    class Meta:
        abstract = True


class Nodo(BaseModel, BaseContatoModel, LogicDeletable):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(u"Nome", max_length=50, blank=True, null=True)
    quem_sou = models.TextField(u"Quem Sou?", max_length=2000, blank=True, null=True)
    carteira = models.CharField(u"Hash Carteira", max_length=42, blank=True, null=True)
    imagem = models.ImageField(upload_to="imagens/nodo/fotos", null=True, blank=True, help_text=u"Dimensões da imagem: %d pixels x %d pixels" % (NODO_TAMANHO_IMAGEM_LISTAGEM_LARGURA, NODO_TAMANHO_IMAGEM_LISTAGEM_ALTURA))
    telefone = models.CharField(u"Telefone", max_length=42, null=True, blank=True)

    def get_tracking_url(self):
        if self.carteira:
            return "https://api.qrserver.com/v1/create-qr-code/?size=130x130&bgcolor=21efe9&color=111c3c&data=https://etherscan.io/address/%s" % self.carteira
        return None

    history = HistoricalRecords()


class Nodos(BaseModel, BaseContatoModel, LogicDeletable):

    criado_por = models.ForeignKey(User, null=True)
    nome = models.CharField(u"Nome da Comunidade", max_length=50)
    slug = AutoSlugField(populate_from='nome')
    imagem = models.ImageField(upload_to="imagens/nodos/listagem", null=True, blank=True, help_text=u"Dimensões da imagem: %d pixels x %d pixels" % (NODOS_TAMANHO_IMAGEM_LISTAGEM_LARGURA, NODOS_TAMANHO_IMAGEM_LISTAGEM_ALTURA))
    resumo = models.CharField(u"Resumo", max_length=140, null=True, blank=True)
    descricao = models.TextField(u"Descrição", null=True, blank=True)

    history = HistoricalRecords()

    def __unicode__(self):
        return u"%s" % self.nome


class Objeto(BaseModel, BaseContatoModel, LogicDeletable):

    criado_por = models.ForeignKey(User, null=True)
    nodos = models.ForeignKey(Nodos)
    nome = models.CharField(u"Nome do Objeto", max_length=50, null=True, blank=True)
    slug = AutoSlugField(populate_from='nome')
    imagem = models.ImageField(upload_to="imagens/objetos/listagem", null=True, blank=True, help_text=u"Dimensões da imagem: %d pixels x %d pixels" % (OBJETO_TAMANHO_IMAGEM_LISTAGEM_LARGURA, OBJETO_TAMANHO_IMAGEM_LISTAGEM_ALTURA))
    descricao = models.TextField(u"Descrição", null=True, blank=True)

    history = HistoricalRecords()

    def __unicode__(self):
        return u"%s" % self.nome


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Nodo.objects.create(user=instance)
    instance.nodo.save()


class Saldo(models.Model):

    carteira = models.CharField(u"Hash da Carteira", max_length=42, unique=True)
    total = models.FloatField()

    def __unicode__(self):
        return u"%s: %0.6f" % self.nome
