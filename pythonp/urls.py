"""pythonp URL Configuration

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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('gamesp.urls')),
    #어플간의 주소전달은, 상위 레벨에서 include를 시켜줘야 한다?
    url(r'^tesorproj/', include('tesorproj.urls')),
    url(r'^tensorapp/', include('tensorapp.urls')),
#    url(r'^game/', include('game.urls')),
 #  url(r'', include('spider_v1.py')),
]
