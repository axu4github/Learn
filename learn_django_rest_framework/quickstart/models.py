# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.


class Query(models.Model):
    """docstring for Query"""
    context = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    language = models.CharField(
        choices=settings.LANGUAGE_CHOICES, default='sql', max_length=100)
    formated = models.CharField(
        blank=False, max_length=1000, default='')  # 格式化后的查询内容
    description = models.CharField(blank=True, max_length=100)  # 查询描述
    owner = models.CharField(blank=False, max_length=30, default='')  # 执行/创建 人

    class Meta:
        ordering = ('-created',)
