# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-22 10:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GuavaApp', '0005_usuario_arboles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adopcion',
            name='hechaPor',
        ),
        migrations.AddField(
            model_name='adopcion',
            name='adoptadaPor',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='adoptante', to='GuavaApp.Usuario'),
        ),
        migrations.AddField(
            model_name='adopcion',
            name='creadaPor',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='duenio', to='GuavaApp.Usuario'),
        ),
        migrations.AddField(
            model_name='adopcion',
            name='fechaCreacion',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='peticion',
            name='arbolesTotales',
            field=models.IntegerField(default=0),
        ),
    ]
