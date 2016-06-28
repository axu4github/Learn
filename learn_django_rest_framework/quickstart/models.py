from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Query(models.Model):
    """docstring for Query"""
    context = models.CharField(blank=False, max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    language = models.CharField(default='sql', max_length=100)

    class Meta:
        ordering = ('created',)
