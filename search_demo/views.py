# -*- coding: utf-8 -*-
from django.shortcuts import render


#搜索功能
def mysearch(request):
    return render(request,'search_demo/mysearch.html')




