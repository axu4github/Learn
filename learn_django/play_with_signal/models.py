# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Foo(models.Model):

    foo = models.CharField(max_length=20)
    bar = models.CharField(max_length=30)

    def post_save(self):
        print "this is post save function."

    def __unicode__(self):
        return "{0}, {1}".format(self.foo, self.bar)
