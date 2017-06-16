# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views import generic
from .models import Users


class UserIndexView(generic.ListView):
    template_name = 'users/index.html'
    context_object_name = 'all_users'

    def get_queryset(self):
        """
        默认返回所有用户
        """
        return Users.objects.all().order_by('-date_joined')


class UserDetailView(generic.DetailView):
    model = Users
    template_name = 'users/detail.html'
