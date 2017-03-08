from django.conf.urls import url
from .views import menu, list_restaurants, comment

urlpatterns = [
    url(r'^$', list_restaurants),
    url(r'^menu/(?P<id>\d{1,5})/$', menu),
    url(r'^comment/(\d{1,5})/$', comment),
]