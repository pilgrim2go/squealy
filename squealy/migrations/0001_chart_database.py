# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-09 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squealy', 'default_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='database',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]