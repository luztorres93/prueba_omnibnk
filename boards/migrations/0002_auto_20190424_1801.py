# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-04-24 23:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='store',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='updated_at',
        ),
    ]
