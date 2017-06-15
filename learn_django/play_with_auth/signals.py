# -*- coding: utf-8 -*-
from .models import Users
from django.db.models.signals import post_save
from django.dispatch import receiver


def common_post_save(sender, instance, **kwargs):
    print "This is common post save function."


@receiver(post_save, sender=Users)  # 修饰器写法
def post_foo_save(sender, instance, **kwargs):
    if hasattr(instance, "post_save"):
        instance.post_save()
    else:
        common_post_save(sender, instance, **kwargs)
