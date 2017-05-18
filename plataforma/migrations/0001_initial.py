# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 14:02
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
            name='HistoricalNodo',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('updated', models.DateTimeField(blank=True, editable=False)),
                ('excluido', models.BooleanField(db_index=True, default=False)),
                ('excluido_em', models.DateTimeField(blank=True, null=True)),
                ('quem_sou', models.TextField(blank=True, max_length=500, null=True, verbose_name='Quem Sou?')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('excluido_por', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical nodo',
            },
        ),
        migrations.CreateModel(
            name='HistoricalNodos',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('updated', models.DateTimeField(blank=True, editable=False)),
                ('excluido', models.BooleanField(db_index=True, default=False)),
                ('excluido_em', models.DateTimeField(blank=True, null=True)),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='nome')),
                ('imagem_listagem', models.TextField(blank=True, max_length=100, null=True)),
                ('imagem_detalhes', models.TextField(blank=True, max_length=100, null=True)),
                ('titulo', models.CharField(blank=True, max_length=50, null=True, verbose_name='T\xedtulo')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descri\xe7\xe3o')),
                ('contato_facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('contato_whatsapp', models.URLField(blank=True, null=True, verbose_name='WhatsApp')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('excluido_por', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical nodos',
            },
        ),
        migrations.CreateModel(
            name='HistoricalObjeto',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('updated', models.DateTimeField(blank=True, editable=False)),
                ('excluido', models.BooleanField(db_index=True, default=False)),
                ('excluido_em', models.DateTimeField(blank=True, null=True)),
                ('nome', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nome')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='nome')),
                ('imagem_listagem', models.TextField(blank=True, max_length=100, null=True)),
                ('imagem_detalhes', models.TextField(blank=True, max_length=100, null=True)),
                ('titulo', models.CharField(blank=True, max_length=50, null=True, verbose_name='T\xedtulo')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descri\xe7\xe3o')),
                ('contato_facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('contato_whatsapp', models.URLField(blank=True, null=True, verbose_name='WhatsApp')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('excluido_por', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical objeto',
            },
        ),
        migrations.CreateModel(
            name='Nodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('excluido', models.BooleanField(db_index=True, default=False)),
                ('excluido_em', models.DateTimeField(blank=True, null=True)),
                ('quem_sou', models.TextField(blank=True, max_length=500, null=True, verbose_name='Quem Sou?')),
                ('excluido_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nodo_excluido_por', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
                ('imagem_listagem', models.ImageField(blank=True, null=True, upload_to='imagens/nodos/listagem')),
                ('imagem_detalhes', models.ImageField(blank=True, null=True, upload_to='imagens/nodos/detalhes')),
                ('titulo', models.CharField(blank=True, max_length=50, null=True, verbose_name='T\xedtulo')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descri\xe7\xe3o')),
                ('contato_facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('contato_whatsapp', models.URLField(blank=True, null=True, verbose_name='WhatsApp')),
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
                ('imagem_listagem', models.ImageField(blank=True, null=True, upload_to='imagens/objetos/listagem')),
                ('imagem_detalhes', models.ImageField(blank=True, null=True, upload_to='imagens/objetos/detalhes')),
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
        migrations.AddField(
            model_name='historicalobjeto',
            name='nodos',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='plataforma.Nodos'),
        ),
    ]
