# -*- coding: utf-8 -*-
from django.shortcuts import render
from search_demo.models import Event, UserProfile
import random
import json
#搜索功能
def mysearch(request):
    return render(request,'search_demo/mysearch.html')


def add(request,ids):
    _user = UserProfile.objects.get(id=2003)
    id = ids.split('@')
    for i in id:
        try:
            _user.associate.add(i)
        except:
            pass
    event = []
    for curid in id:
        cur_event = Event.objects.get(id=curid)
        event.append(cur_event.e_name)
    content = {
        'events':','.join(event)
    }
    return render(request,'search_demo/add.html',content)


def show_events(request):
    # content = dict(zip(map(str, range(10)),range(10)))
    events = []
    for j in range(10):
        cur_events = []
        id = []
        for i in range(3):
            cur = random.randint(22,422)
            id.append(str(cur))
            cur_event = Event.objects.get(id=cur)
            cur_events.append(cur_event.e_name.strip())
        events.append({'name':' '.join(cur_events),'ids':'@'.join(id)})
    content = {
        'events':events
    }
        # key = str(i)
        # content[key] = {'name':' '.join(events),'ids':'@'.join(id)}
    return render(request,'search_demo/show.html',content)
