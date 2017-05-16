# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from autoslug import AutoSlugField
from django.db import models
from simple_history.models import HistoricalRecords

from common.models import BaseModel, LogicDeletable


class Nodo(BaseModel, LogicDeletable):

    history = HistoricalRecords()


class Nodos(BaseModel, LogicDeletable):

    nome = models.CharField(u"Nome", max_length=50)
    slug = AutoSlugField(populate_from='nome')
    imagem_listagem = models.ImageField(upload_to="imagens/nodos/listagem", null=True, blank=True)
    imagem_detalhes = models.ImageField(upload_to="imagens/nodos/detalhes", null=True, blank=True)
    titulo = models.CharField(u"Título", max_length=50, null=True, blank=True)
    descricao = models.TextField(u"Descrição", null=True, blank=True)

    contato_facebook = models.URLField(u"Facebook", null=True, blank=True)
    contato_whatsapp = models.URLField(u"WhatsApp", null=True, blank=True)

    history = HistoricalRecords()

    def __unicode__(self):
        return u"%s" % self.nome


class Objeto(BaseModel, LogicDeletable):

    nodos = models.ForeignKey(Nodos)
    nome = models.CharField(u"Nome", max_length=50, null=True, blank=True)
    slug = AutoSlugField(populate_from='nome')
    imagem_listagem = models.ImageField(upload_to="imagens/objetos/listagem", null=True, blank=True)
    imagem_detalhes = models.ImageField(upload_to="imagens/objetos/detalhes", null=True, blank=True)
    titulo = models.CharField(u"Título", max_length=50, null=True, blank=True)
    descricao = models.TextField(u"Descrição", null=True, blank=True)

    contato_facebook = models.URLField(u"Facebook", null=True, blank=True)
    contato_whatsapp = models.URLField(u"WhatsApp", null=True, blank=True)

    history = HistoricalRecords()

    def __unicode__(self):
        return u"%s" % self.nome
