# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('satti', '0010_auto_20161117_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatuser',
            name='profile_text',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
