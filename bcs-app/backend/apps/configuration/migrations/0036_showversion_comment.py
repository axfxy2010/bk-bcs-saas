# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-11-25 03:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0035_auto_20200702_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='showversion',
            name='comment',
            field=models.TextField(default='', verbose_name='版本说明'),
        ),
    ]
