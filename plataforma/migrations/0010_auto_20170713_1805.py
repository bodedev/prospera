# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0009_saldo'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalnodo',
            name='history_change_reason',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historicalnodos',
            name='history_change_reason',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historicalobjeto',
            name='history_change_reason',
            field=models.CharField(max_length=100, null=True),
        ),
    ]