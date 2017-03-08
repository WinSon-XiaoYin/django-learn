from django.conf.urls import url
from .views import menu, list_restaurants, comment

urlpatterns = [
    url(r'^list/$', list_restaurants),
    url(r'^menu/(?P<id>\d{1,5})/$', menu),
    url(r'^menu/$', menu, {'id': '1'}),
    url(r'^comment/(\d{1,5})/$', comment),
]