# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-01 01:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_review_songartists'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='query',
            field=models.CharField(default='No query', max_length=100),
        ),
    ]
