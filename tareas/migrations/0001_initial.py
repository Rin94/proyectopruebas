# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tareas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=60, verbose_name='nombre')),
                ('precio', models.FloatField(verbose_name='precio')),
                ('descripcion', models.CharField(max_length=120, verbose_name='descripcion')),
                ('detalles', models.CharField(max_length=120, null=True, verbose_name='detalles', blank=True)),
            ],
        ),
    ]
