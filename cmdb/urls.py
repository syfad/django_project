"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from cmdb import views

from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('home/', views.home),
    path('modelbox/', views.modelbox),
    #path('detail/', views.detail),

    re_path(r'useredit-(?P<nid>\d+)', views.useredit),
    re_path(r'detail-(\d+).html', views.detail),
    re_path(r'userdel-(?P<nid>\d+)', views.userdelete),

    re_path('host/', views.host),
    re_path('app/', views.app),
    re_path('ajax_add_app/', views.ajax_add_app),
    re_path('user_list/', views.user_list),


    path('index/', views.index),
    path('register/', views.register),

    #re_path(r'^detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.index),

    re_path(r'^asdfsdf/(\d+)/(\d+)', views.index, name='indexx'),
    re_path(r'^asdfsdf/(?P<nid>\d+)/(?P<uid>\d+)', views.index, name='indexx'),

    #re_path(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL}),
    #re_path(r'^cmdb/static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),


    #re_path(r'^asdsafd/', views.index, name='index')
]

