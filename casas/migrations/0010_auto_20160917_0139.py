# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-17 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casas', '0009_auto_20160917_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casa',
            name='deposito',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='casa',
            name='plantas',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='casa',
            name='recamaras',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
