# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-08 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Investigador', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investigador',
            name='Coordenadas',
            field=models.CharField(blank=True, max_length=450),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='Direccion',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='Telefono',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
