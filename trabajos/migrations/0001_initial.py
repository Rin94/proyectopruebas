# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
        ('tareas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='lista_articulos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField(verbose_name='cantidad')),
                ('costo', models.FloatField(verbose_name='costo')),
                ('detalles', models.CharField(max_length=120, null=True, verbose_name='detalles', blank=True)),
                ('tarea', models.ForeignKey(to='tareas.tareas')),
            ],
        ),
        migrations.CreateModel(
            name='trabajos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicio', models.DateTimeField(auto_now_add=True, verbose_name='fecha_inicio')),
                ('fehca_final', models.DateTimeField(auto_now=True, verbose_name='fecha_fin')),
                ('detalles', models.CharField(max_length=120, verbose_name='detalles')),
                ('cliente', models.ForeignKey(to='clientes.clientes')),
            ],
        ),
        migrations.AddField(
            model_name='lista_articulos',
            name='trabajo',
            field=models.ForeignKey(to='trabajos.trabajos'),
        ),
    ]
