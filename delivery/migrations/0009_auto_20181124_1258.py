# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-11-24 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0008_auto_20181122_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverytask',
            name='priority',
            field=models.IntegerField(default=1),
        ),
    ]