# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-11 04:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_demo', '0002_auto_20180711_0340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='account',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='associate',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='associate',
            field=models.ManyToManyField(blank=True, max_length=50, to='search_demo.Event', verbose_name='\u5173\u8054\u4e8b\u4ef6'),
        ),
    ]