# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from simple_history.models import HistoricalRecords

from common.models import BaseModel, LogicDeletable
from plataforma.constants import NODOS_TAMANHO_IMAGEM_LISTAGEM_LARGURA, NODOS_TAMANHO_IMAGEM_LISTAGEM_ALTURA, NODOS_TAMANHO_IMAGEM_DETALHES_LARGURA, NODOS_TAMANHO_IMAGEM_DETALHES_ALTURA
from plataforma.constants import OBJETO_TAMANHO_IMAGEM_LISTAGEM_LARGURA, OBJETO_TAMANHO_IMAGEM_LISTAGEM_ALTURA, OBJETO_TAMANHO_IMAGEM_DETALHES_LARGURA, OBJETO_TAMANHO_IMAGEM_DETALHES_ALTURA


class Nodo(BaseModel, LogicDeletable):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    quem_sou = models.TextField(u"Quem Sou?", max_length=500, blank=True, null=True)
    history = HistoricalRecords()


class Nodos(BaseModel, LogicDeletable):

    criado_por = models.ForeignKey(User, null=True)
    nome = models.CharField(u"Nome", max_length=50)
    slug = AutoSlugField(populate_from='nome')
    imagem_listagem = models.ImageField(upload_to="imagens/nodos/listagem", null=True, blank=True, help_text=u"Dimensões da imagem: %d pixels x %d pixels" % (NODOS_TAMANHO_IMAGEM_LISTAGEM_LARGURA, NODOS_TAMANHO_IMAGEM_LISTAGEM_ALTURA))
    imagem_detalhes = models.ImageField(upload_to="imagens/nodos/detalhes", null=True, blank=True, help_text=u"Dimensões da imagem: %d pixels x %d pixels" % (NODOS_TAMANHO_IMAGEM_DETALHES_LARGURA, NODOS_TAMANHO_IMAGEM_DETALHES_ALTURA))
    titulo = models.CharField(u"Título", max_length=50, null=True, blank=True)
    descricao = models.TextField(u"Descrição", null=True, blank=True)

    contato_facebook = models.URLField(u"Facebook", null=True, blank=True)
    contato_whatsapp = models.URLField(u"WhatsApp", null=True, blank=True)

    history = HistoricalRecords()

    def __unicode__(self):
        return u"%s" % self.nome


class Objeto(BaseModel, LogicDeletable):

    criado_por = models.ForeignKey(User, null=True)
    nodos = models.ForeignKey(Nodos)
    nome = models.CharField(u"Nome", max_length=50, null=True, blank=True)
    slug = AutoSlugField(populate_from='nome')
    imagem_listagem = models.ImageField(upload_to="imagens/objetos/listagem", null=True, blank=True, help_text=u"Dimensões da imagem: %d pixels x %d pixels" % (OBJETO_TAMANHO_IMAGEM_LISTAGEM_LARGURA, OBJETO_TAMANHO_IMAGEM_LISTAGEM_ALTURA))
    imagem_detalhes = models.ImageField(upload_to="imagens/objetos/detalhes", null=True, blank=True, help_text=u"Dimensões da imagem: %d pixels x %d pixels" % (OBJETO_TAMANHO_IMAGEM_DETALHES_LARGURA, OBJETO_TAMANHO_IMAGEM_DETALHES_ALTURA))
    titulo = models.CharField(u"Título", max_length=50, null=True, blank=True)
    descricao = models.TextField(u"Descrição", null=True, blank=True)

    contato_facebook = models.URLField(u"Facebook", null=True, blank=True)
    contato_whatsapp = models.URLField(u"WhatsApp", null=True, blank=True)

    history = HistoricalRecords()

    def get_endereco_sala(self):
        return u"https://www.appear.in/prospera-%s" % self.criado_por.username

    def __unicode__(self):
        return u"%s" % self.nome


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Nodo.objects.create(user=instance)
    instance.nodo.save()
