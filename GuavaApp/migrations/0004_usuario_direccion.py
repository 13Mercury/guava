# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-22 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuavaApp', '0003_auto_20171121_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(default='', max_length=200),
        ),
    ]
