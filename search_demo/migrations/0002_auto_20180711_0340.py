# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-11 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_demo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='account',
        ),
        migrations.AddField(
            model_name='event',
            name='account',
            field=models.ManyToManyField(blank=True, to='search_demo.UserProfile', verbose_name='\u53c2\u4e0e\u7528\u6237'),
        ),
    ]
