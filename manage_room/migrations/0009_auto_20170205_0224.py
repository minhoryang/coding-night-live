# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-04 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_room', '0008_auto_20170203_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='title',
            field=models.CharField(default='Unnamed slide', max_length=35),
        ),
    ]