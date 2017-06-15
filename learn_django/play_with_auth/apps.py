# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class PlayWithAuthConfig(AppConfig):
    name = 'play_with_auth'

    def ready(self):
        import play_with_auth.signals