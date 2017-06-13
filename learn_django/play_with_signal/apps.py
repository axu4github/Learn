# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.apps import AppConfig


class PlayWithSignalConfig(AppConfig):
    name = 'play_with_signal'

    def ready(self):
        import play_with_signal.signals
