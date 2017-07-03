# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    # 解决 was_published_recently 列，在 Admin 页面无法排序问题
    # more read:
    #   http://python.usyiyi.cn/translate/django_182/ref/contrib/admin/index.html#django.contrib.admin.ModelAdmin.list_display
    was_published_recently.admin_order_field = 'pub_date'  # 支持排序（升序）
    # was_published_recently.admin_order_field = '-pub_date' # 支持排序（降序）
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'  # 表头显示内容

    def __unicode__(self):              # __unicode__ on Python 2
        return self.question_text

    class Meta:
        permissions = (
            ("riskview_all", "Can see all the pages"),
        )


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.choice_text
