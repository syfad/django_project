#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018
# @Author  : SunYunfeng(sun_admin@126.com)
# @Disc    : 
# @Disc    : support python 2.x and 3.x

from django.contrib import admin
from django.urls import path, re_path, include
from app02 import views



urlpatterns = [
    re_path(r'^newlogin/', views.newlogin),
    re_path(r'^orm/', views.orm),
]