# -*- coding: utf-8 -*-
from .models import Foo, Bar
from django.db.models.signals import post_save
from django.dispatch import receiver


def common_post_save(sender, instance, **kwargs):
    print "This is common post save function."


@receiver(post_save, sender=Foo)  # 修饰器写法
@receiver(post_save, sender=Bar)  # 修饰器写法
def post_foo_save(sender, instance, **kwargs):
    if hasattr(instance, "post_save"):
        instance.post_save()
    else:
        common_post_save(sender, instance, **kwargs)

# 初级写法
# post_save.connect(post_foo_save, sender=Foo)
