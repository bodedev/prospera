# -*- coding: utf-8 -*-


from __future__ import unicode_literals


from django.contrib import admin


from plataforma.forms import NodosForm, ObjetoForm
from plataforma.models import Nodos, Objeto


@admin.register(Nodos)
class NodosAdmin(admin.ModelAdmin):

    form = NodosForm
    list_display = ("id", "nome")


@admin.register(Objeto)
class ObjetoAdmin(admin.ModelAdmin):

    form = ObjetoForm
    list_display = ("id", "nodos", "nome")


admin.site.site_header = u"Administração Prospera"
admin.site.site_title = u"Administração Prospera"
admin.site.index_title = u"Administração"
