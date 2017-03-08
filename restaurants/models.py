# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'餐馆'
        verbose_name_plural = u'餐馆'

class Food(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=3, decimal_places=0)
    comment = models.CharField(max_length=50, blank=True)
    is_spicy = models.BooleanField(default=False)
    restaurant = models.ForeignKey(Restaurant)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'食物'
        verbose_name_plural = u'食物'
        ordering = ['price']

class Comment(models.Model):
    content = UEditorField('评论内容', height=300, width=1000,
                           default=u'', blank=True, imagePath="uploads/images/",
                           toolbars='besttome', filePath='uploads/files/')
    visitor = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date_time = models.DateTimeField()
    restaurant = models.ForeignKey(Restaurant)

    def __unicode__(self):
        return self.visitor

    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = u'评论'
        ordering = ['date_time']
        permissions = (
            ('can_comment', 'Can comment'),
        )