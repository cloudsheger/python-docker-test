# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-22 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20180522_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcepage',
            name='embedSRC',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
