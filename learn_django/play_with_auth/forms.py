# -*- coding: utf-8 -*-
from django.forms import ModelForm
from models import Users


class UserForm(ModelForm):
    """用户表单"""

    class Meta:
        model = Users
        fields = "__all__"
