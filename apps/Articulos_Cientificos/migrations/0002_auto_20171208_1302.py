# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-08 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articulos_Cientificos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulos_cientificos',
            name='Anio',
            field=models.IntegerField(null=True),
        ),
    ]
