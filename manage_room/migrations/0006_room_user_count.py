# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-30 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_room', '0005_auto_20170129_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='user_count',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
