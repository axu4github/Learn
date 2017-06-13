from .models import Foo
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Foo)  # 修饰器写法
def post_foo_save(sender, instance, **kwargs):
    instance.post_save()

# 初级写法
# post_save.connect(post_foo_save, sender=Foo)
