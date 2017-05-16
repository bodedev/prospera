# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 20:44
from __future__ import unicode_literals

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Nodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('excluido', models.BooleanField(db_index=True, default=False)),
                ('excluido_em', models.DateTimeField(blank=True, null=True)),
                ('excluido_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nodo_excluido_por', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Nodos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('excluido', models.BooleanField(db_index=True, default=False)),
                ('excluido_em', models.DateTimeField(blank=True, null=True)),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='nome')),
                ('titulo', models.CharField(blank=True, max_length=50, null=True, verbose_name='T\xedtulo')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descri\xe7\xe3o')),
                ('excluido_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nodos_excluido_por', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Objeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('excluido', models.BooleanField(db_index=True, default=False)),
                ('excluido_em', models.DateTimeField(blank=True, null=True)),
                ('nome', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nome')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='nome')),
                ('titulo', models.CharField(blank=True, max_length=50, null=True, verbose_name='T\xedtulo')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descri\xe7\xe3o')),
                ('contato_facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('contato_whatsapp', models.URLField(blank=True, null=True, verbose_name='WhatsApp')),
                ('excluido_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='objeto_excluido_por', to=settings.AUTH_USER_MODEL)),
                ('nodos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataforma.Nodos')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]