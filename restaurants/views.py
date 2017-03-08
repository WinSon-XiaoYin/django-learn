# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from restaurants.models import Restaurant, Food, Comment
from django.utils import timezone
from django.template import RequestContext
from restaurants.forms import CommentForm
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required

def menu(request):
    restaurant = Restaurant.objects.get(id=2)
    return render_to_response('menu.html', locals())

def meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(k, v))
    return HttpResponse('<table>{0}</table>'.format('\n'.join(html)))


@login_required
def list_restaurants(request):
    # if not request.user.is_authenticated():
    #     return HttpResponseRedirect('/accounts/login/?next={0}'.format(request.path))
    restaurants = Restaurant.objects.all()
    return render_to_response('restaurants_list.html', RequestContext(request, locals()))

def comment(request, id):
    if id:
        r = Restaurant.objects.get(id=id)
    else:
        return HttpResponseRedirect('/restaurants_list')
    if request.POST:
        f = CommentForm(request.POST)
        if f.is_valid():
            visitor = request.POST['visitor']
            content = request.POST['content']
            email = request.POST['email']
            date_time = timezone.localtime(timezone.now())

            c = Comment.objects.create(
                visitor=visitor,
                email=email,
                content=content,
                date_time=date_time,
                restaurant=r
            )
            f = CommentForm(initial={'content': '我没意见'})
    else:
        f = CommentForm(initial={'content': '我没意见'})
    return render_to_response('comments.html', RequestContext(request, locals()))


def set_c(request):
    response = HttpResponse('Set your lucky_number as 8')
    response.set_cookie('lucky_number', 8)
    return response

def get_c(request):
    if 'lucky_number' in request.COOKIES:
        return HttpResponse('Your lucky_number is {0}'.format(request.COOKIES['lucky_number']))
    else:
        return HttpResponse('No cookies.')


def session_test(request):
    sid = request.COOKIES['sessionid']
    sid2 = request.session.session_key
    s = Session.objects.get(pk=sid)
    s_info = 'Session ID:' + sid + '<br>SessionID2:' + sid2 + '<br>Expire_date:' + str(s.expire_date) + '<br>Data:' + str(s.get_decoded())
    return HttpResponse(s_info)