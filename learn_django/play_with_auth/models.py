# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser


class Tenants(models.Model):
    """租户表"""
    name = models.CharField(max_length=100, default="")
    code = models.CharField(max_length=20, default="")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name


class Users(AbstractUser):
    """扩展用户表"""
    password_expired = models.BigIntegerField(default=0)  # timestamp
    token_expired = models.BigIntegerField(default=0)  # timestamp
    is_active = models.BooleanField(default=True)
    token = models.CharField(max_length=100, default="")  # user_token
    tenant = models.OneToOneField(Tenants, default=0)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.username
