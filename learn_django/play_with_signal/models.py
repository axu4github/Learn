# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Foo(models.Model):

    foo = models.CharField(max_length=20)

    def post_save(self):
        print "this is Class Foo post save function."

    def __unicode__(self):
        return "{0}".format(self.foo)


class Bar(models.Model):

    bar = models.CharField(max_length=30)

    def __unicode__(self):
        return "{0}".format(self.bar)
