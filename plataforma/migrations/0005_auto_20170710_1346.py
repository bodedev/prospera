# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-10 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0004_auto_20170710_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalnodo',
            name='foto',
            field=models.TextField(blank=True, help_text='Dimens\xf5es da imagem: 400 pixels x 400 pixels', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='nodo',
            name='foto',
            field=models.ImageField(blank=True, help_text='Dimens\xf5es da imagem: 400 pixels x 400 pixels', null=True, upload_to='imagens/nodo/fotos'),
        ),
    ]