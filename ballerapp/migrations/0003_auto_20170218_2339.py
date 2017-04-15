# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 22:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ballerapp', '0002_auto_20170218_2337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adresse',
            name='datetime',
        ),
        migrations.AddField(
            model_name='adresse',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
    ]
