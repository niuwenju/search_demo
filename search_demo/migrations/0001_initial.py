# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-10 16:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('e_name', models.CharField(max_length=20, verbose_name='\u4e8b\u4ef6\u540d')),
                ('e_address', models.CharField(max_length=50, verbose_name='\u4e8b\u4ef6\u5730\u5740')),
                ('e_balance', models.CharField(max_length=20, verbose_name='\u4f59\u989d')),
                ('attr', models.CharField(blank=True, choices=[('c', '\u56fd\u5185\u5927\u5b66'), ('f', '\u56fd\u5916\u5927\u5b66'), ('g', '\u6e38\u620f'), ('fs', '\u5973\u660e\u661f'), ('ms', '\u7537\u660e\u661f'), ('bo', '\u8bfb\u4e66'), ('sp', '\u4f53\u80b2'), ('fi', '\u8d22\u7ecf'), ('mu', '\u97f3\u4e50'), ('mo', '\u7535\u5f71')], max_length=20, null=True, verbose_name='\u4e8b\u4ef6\u5c5e\u6027')),
            ],
            options={
                'verbose_name': '\u4e8b\u4ef6\u4fe1\u606f',
                'verbose_name_plural': '\u4e8b\u4ef6\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='\u7528\u6237\u540d')),
                ('address', models.CharField(max_length=50, verbose_name='\u7528\u6237\u5730\u5740')),
                ('balance', models.FloatField(max_length=20, verbose_name='\u7528\u6237\u4f59\u989d')),
                ('associate', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u5173\u8054\u4e8b\u4ef6')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237\u4fe1\u606f',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='search_demo.UserProfile', verbose_name='\u53c2\u4e0e\u7528\u6237'),
        ),
    ]