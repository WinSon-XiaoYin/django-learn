# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from restaurants.models import Restaurant, Food, Comment
from django.utils import timezone
from django.template import RequestContext
from restaurants.forms import CommentForm
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required

def menu(request, id):
    restaurant = Restaurant.objects.get(id=id)
    return render_to_response('menu.html', locals())


@login_required
def list_restaurants(request):
    restaurants = Restaurant.objects.all()
    return render_to_response('restaurants_list.html', RequestContext(request, locals()))

def comment(request, id):
    if id:
        r = Restaurant.objects.get(id=id)
        user = request.user
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