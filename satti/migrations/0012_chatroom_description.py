# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('satti', '0011_chatuser_profile_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
