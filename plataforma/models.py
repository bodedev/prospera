# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from simple_history.models import HistoricalRecords

from common.models import BaseModel, LogicDeletable


class Nodo(BaseModel, LogicDeletable):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    quem_sou = models.TextField(u"Quem Sou?", max_length=500, blank=True, null=True)
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


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Nodo.objects.create(user=instance)
    instance.nodo.save()
