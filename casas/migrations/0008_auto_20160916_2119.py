# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casas', '0007_casa_municipio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casa',
            name='municipio',
            field=models.CharField(default='Municipio', max_length=60),
        ),
    ]
