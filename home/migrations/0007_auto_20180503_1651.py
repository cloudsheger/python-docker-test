# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-03 16:51
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_homepage_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='intro',
        ),
        migrations.AddField(
            model_name='homepage',
            name='intitiative1Body',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intitiative1Link',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intitiative1Title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intitiative2Body',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intitiative2Link',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intitiative2Title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intitiative3Body',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intitiative3Link',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intitiative3Title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=models.CharField(default='The California Bat Working Group (CBWG) is composed of individuals dedicated to bat research, education, management, and conservation. Our mission is to facilitate communication regarding bat ecology, distribution, and research techniques, and provide a forum to discuss conservation and management strategies, provide technical assistance, and encourage education.', max_length=500),
        ),
    ]
