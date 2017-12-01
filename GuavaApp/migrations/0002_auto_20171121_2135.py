# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-22 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuavaApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='descripcion',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='usuario',
            name='pagina',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='image',
            field=models.ImageField(default='/media/2.jpg', upload_to='Usuarios'),
        ),
    ]