# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=35, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=45, verbose_name='last_name')),
                ('gender', models.IntegerField(verbose_name='gender')),
                ('email', models.EmailField(max_length=60, verbose_name='email')),
                ('phone_number', models.CharField(max_length=15, verbose_name='phone')),
                ('num_direccion', models.IntegerField(verbose_name='numero_casa')),
                ('calle', models.CharField(max_length=45, verbose_name='calle')),
                ('colonia', models.CharField(max_length=45, verbose_name='colonia')),
                ('codigo_postal', models.IntegerField(verbose_name='codigo_postal')),
                ('municipio', models.CharField(max_length=30, verbose_name='municipio')),
                ('estado', models.CharField(max_length=30, verbose_name='estado')),
                ('pais', models.CharField(max_length=30, verbose_name='pais')),
                ('detalles', models.CharField(max_length=120, null=True, verbose_name='detalles', blank=True)),
            ],
        ),
    ]
