# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from autoslug import AutoSlugField
from django.db import models

from common.models import BaseModel, LogicDeletable


class Nodo(BaseModel, LogicDeletable):

    pass


class Nodos(BaseModel, LogicDeletable):

    nome = models.CharField(u"Nome", max_length=50)
    slug = AutoSlugField(populate_from='nome')
    titulo = models.CharField(u"Título", max_length=50, null=True, blank=True)
    descricao = models.TextField(u"Descrição", null=True, blank=True)

    def __unicode__(self):
        return u"%s" % self.nome


class Objeto(BaseModel, LogicDeletable):

    nodos = models.ForeignKey(Nodos)
    nome = models.CharField(u"Nome", max_length=50, null=True, blank=True)
    slug = AutoSlugField(populate_from='nome')
    titulo = models.CharField(u"Título", max_length=50, null=True, blank=True)
    descricao = models.TextField(u"Descrição", null=True, blank=True)

    contato_facebook = models.URLField(u"Facebook", null=True, blank=True)
    contato_whatsapp = models.URLField(u"WhatsApp", null=True, blank=True)

    def __unicode__(self):
        return u"%s" % self.nome
