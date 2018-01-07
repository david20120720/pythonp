"""tensorproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
#from tensorproject.views import helloworld,spidergame,jinjagame
from tensorapp.views import *



urlpatterns = [
#    url(r'^/tesorproj/write/',write,name='write'),
#    url(r'^/tesorproj/list"/',list,name='list'),
#    url(r'^/tesorproj/view"/(?P<num>[0-9]+)/$',view,name='view'),

# 상위레벨에서 include 된 상태에서는  위와같이 반복적으로 tesorproj등을 기록하면 않됨
    url(r'^',tensorapp ,name='tensorapp'),
    url(r'^write/',write,name='write'),

]
