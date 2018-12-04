# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-11-18 15:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('created_by', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=11)),
            ],
        ),
    ]