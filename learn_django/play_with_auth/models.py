# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Tenants(models.Model):
    """租户表"""
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
