# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-30 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_staticpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='body',
        ),
        migrations.AddField(
            model_name='homepage',
            name='initiativesHeader',
            field=models.CharField(default='Initiatives', max_length=100),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro',
            field=models.CharField(default='The California Bat Working Group (CBWG) is composed of individuals dedicated to bat research, education, management, and conservation. Our mission is to facilitate communication regarding bat ecology, distribution, and research techniques, and provide a forum to discuss conservation and management strategies, provide technical assistance, and encourage education.', max_length=500),
        ),
        migrations.AddField(
            model_name='homepage',
            name='regionalHeader',
            field=models.CharField(default='Regional groups', max_length=100),
        ),
        migrations.AddField(
            model_name='homepage',
            name='updatesHeader',
            field=models.CharField(default='CBWG Updates', max_length=100),
        ),
    ]
