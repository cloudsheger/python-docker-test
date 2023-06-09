# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-22 18:05
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_resourcepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcepage',
            name='embedBody',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resourcepage',
            name='embedIntro',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='resourcepage',
            name='embedTitle',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='resourcepage',
            name='body',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resourcepage',
            name='intro',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
