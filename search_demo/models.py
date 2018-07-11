# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

from search.settings import *


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    e_name = models.CharField(verbose_name='事件名', max_length=20)
    e_address = models.CharField(verbose_name='事件地址', max_length=50)
    e_balance = models. CharField(verbose_name='余额', max_length=20)
    attr = models. CharField(verbose_name='事件属性', choices=(('col',u'国内大学'),('for',u'国外大学'), ('gam', u'游戏'), ('sta', u'明星'), ('sto', u'股票'), ('boo', u'读书'), ('spo', u'体育'), ('car', u'车'), ('mus', u'音乐'), ('mov', u'电影')),max_length=20, null=True, blank=True)
    # account = models.ManyToManyField(UserProfile,verbose_name='参与用户',blank=True)


    def __unicode__(self):
        return self.e_name

    def addtime_format(self):
        return self.addtime.strftime('%Y-%m-%d %H:%M:%S')

    class Meta:
        verbose_name = u'事件信息'
        verbose_name_plural = u'事件信息'


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'e_name', 'e_address', 'e_balance')
    list_display_links = ('e_name',)
    # list_per_page = ADMIN_PAGE_SIZE

    class Meta:
        verbose_name = '事件信息'
        verbose_name_plural = '事件信息'


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='用户名', max_length=20)
    address = models.CharField(verbose_name='用户地址', max_length=50)
    balance = models. FloatField(verbose_name='用户余额', max_length=20)
    associate = models.ManyToManyField(Event, verbose_name='关联事件', max_length=50,blank=True)


    def __unicode__(self):
        return self.name

    def addtime_format(self):
        return self.addtime.strftime('%Y-%m-%d %H:%M:%S')

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = u'用户信息'


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'balance')
    # list_display_links = ('name','address', 'balance')
    # list_per_page = ADMIN_PAGE_SIZE


    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'





admin.site.register(Event, EventAdmin)
admin.site.register(UserProfile, UserProfileAdmin)