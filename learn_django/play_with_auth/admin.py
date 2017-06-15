# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from play_with_auth.models import Users, Tenants

admin.site.register(Users)
admin.site.register(Tenants)
