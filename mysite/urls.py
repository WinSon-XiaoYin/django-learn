"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from restaurants.views import menu, meta, list_restaurants, comment, set_c, get_c, session_test
from views import welcome, index, register
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^menu/$', menu),
    url(r'^meta/$', meta),
    url(r'^welcome', welcome),
    url(r'^restaurants_list', list_restaurants),
    url(r'^comment/(\d{1,5})/$', comment),
    url(r'^set/$', set_c),
    url(r'^get/$', get_c),
    url(r'^session_test/$', session_test),
    url(r'^accounts/login/$', login),
    url(r'^index/$', index),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/register/$', register),
]
