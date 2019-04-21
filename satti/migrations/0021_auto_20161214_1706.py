# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-14 17:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('satti', '0020_auto_20161213_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='description',
            field=models.CharField(blank=True, default="This is the default chatroom description. It is a bit longer than the default text for profiles, and that's intentional.", max_length=200),
        ),
    ]
