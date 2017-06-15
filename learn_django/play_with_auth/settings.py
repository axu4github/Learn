# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from appconf import AppConf


class Settings(AppConf):

    PASSWORD_EXPIRED_DAYS = 90

    class Meta:
        prefix = ""
