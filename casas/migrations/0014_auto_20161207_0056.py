# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-07 00:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casas', '0013_auto_20160917_0402'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='casa',
            options={'ordering': ('fecha',)},
        ),
        migrations.RenameField(
            model_name='casa',
            old_name='depósito',
            new_name='deposito',
        ),
        migrations.RenameField(
            model_name='casa',
            old_name='dirección',
            new_name='direccion',
        ),
        migrations.RenameField(
            model_name='casa',
            old_name='recámaras',
            new_name='recmaras',
        ),
        migrations.RenameField(
            model_name='casa',
            old_name='teléfono',
            new_name='telefono',
        ),
    ]
