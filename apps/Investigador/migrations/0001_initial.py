# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-08 15:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carrera', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='investigador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cedula', models.CharField(blank=True, max_length=10)),
                ('Direccion', models.TextField(blank=True, max_length=500)),
                ('Coordenadas', models.TextField(blank=True, max_length=450)),
                ('Telefono', models.IntegerField(blank=True)),
                ('Genero', models.CharField(blank=True, max_length=100)),
                ('Ciudadania', models.CharField(blank=True, max_length=100)),
                ('carrera', models.ManyToManyField(to='carrera.carrera')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
