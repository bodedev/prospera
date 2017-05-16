# -*- coding: utf-8 -*-


from datetime import datetime

from common.model_managers import SemExcluidosManager, ComExcluidosManager
from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class LogicDeletable(models.Model):
    u"""
        Classe que fornece funcionalidade pra delete lógico de um modelo.
        Pode armazenar quem deletou e quando, também pode reativar o modelo.
        Já possui managers pra filtrar excluídos e não excluídos.
    """
    excluido = models.BooleanField(default=False, db_index=True)
    excluido_por = models.ForeignKey(User, related_name='%(class)s_excluido_por', null=True, blank=True, on_delete=models.SET_NULL)
    excluido_em = models.DateTimeField(null=True, blank=True)

    objects = SemExcluidosManager()
    com_excluidos = ComExcluidosManager()

    def delete(self, using=None):
        self.excluido = True
        self.excluido_em = datetime.now()
        self.save()

    def logic_delete(self, user, using=None):
        self.excluido_por = user
        self.save()
        self.delete(using)

    def reativar(self):
        self.excluido = False
        self.excluido_por = None
        self.excluido_em = None
        self.save()

    class Meta:
        abstract = True
