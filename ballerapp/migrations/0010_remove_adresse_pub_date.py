# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-15 13:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ballerapp', '0009_auto_20170415_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adresse',
            name='pub_date',
        ),
    ]
