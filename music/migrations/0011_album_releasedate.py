# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-02 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0010_song_albumid'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='releaseDate',
            field=models.CharField(blank=True, default='No release date', max_length=20, null=True),
        ),
    ]
