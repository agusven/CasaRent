# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-17 09:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_municpio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='municpio',
            new_name='municipio',
        ),
    ]