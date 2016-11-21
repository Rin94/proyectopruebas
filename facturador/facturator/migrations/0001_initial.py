# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trabajos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='articulos_facturados',
            fields=[
                ('orden', models.ForeignKey(primary_key=True, serialize=False, to='trabajos.lista_articulos', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='factura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_factura', models.DateField(auto_now_add=True, verbose_name='fecha_factura')),
                ('costo_total', models.FloatField(verbose_name='costo_total')),
                ('detalles', models.CharField(max_length=120, null=True, verbose_name='detalles', blank=True)),
                ('job', models.ForeignKey(to='trabajos.trabajos', unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='articulos_facturados',
            name='factura',
            field=models.ForeignKey(to='facturator.factura', unique=True),
        ),
    ]
