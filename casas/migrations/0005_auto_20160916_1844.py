# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casas', '0004_auto_20160911_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='casa',
            name='telefono',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='casa',
            name='amueblada',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='casa',
            name='cochera',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='casa',
            name='patio',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='casa',
            name='precio',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='casa',
            name='servicios',
            field=models.CharField(max_length=140),
        ),
    ]