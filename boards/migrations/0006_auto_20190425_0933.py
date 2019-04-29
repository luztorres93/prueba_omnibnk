# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-04-25 14:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0005_movie_category_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='category_movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='boards.category'),
            preserve_default=False,
        ),
    ]