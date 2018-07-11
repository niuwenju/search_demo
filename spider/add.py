# _*_ coding: utf-8 _*_
import random
import json
from search_demo.models import Event, UserProfile
from utils import function
import itertools


#添加用户与事件的联系
e_list = Event.objects.all()
for i in range(1000):
    curuser = UserProfile.objects.get(id=i)
    cur = random.sample(e_list,150)
    curuser.associate.add(*cur)


#添加模拟用户
def adduser():
    for i in range(2000):
        a = map("".join, list(itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=4)))
        cur_name = a[random.randint(0, 26 ** 4 - 1)]
        _user = UserProfile(
                    name=cur_name,
                    address=function.md5_encode(cur_name),
                    balance=random.uniform(0, 10000.0),
                )
        _user.save()

#添加股票事件
def addsto():
    with open('/home/niuwenju/Desktop/project/source/sto.txt') as f:
        for i in f:
            _user = Event(
                e_name=i.replace('\'', ''),
                e_address=function.md5_encode(i.replace('\'', '')),
                e_balance=random.uniform(0, 10000.0),
                attr='sto'
            )
            _user.save()

#添加电影事件
def adddmov():
    a1 = open('/home/niuwenju/Desktop/project/source/movie.json')
    b = json.load(a1)
    for i in b['subjects']:
        _user = Event(
            e_name=i['title'].encode("utf-8"),
            e_address=function.md5_encode(i['title'].encode("utf-8")),
            e_balance=random.uniform(0,10000.0),
            attr='mov'
        )
        _user.save()
