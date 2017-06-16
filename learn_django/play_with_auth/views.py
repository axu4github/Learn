# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from models import Users
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


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


class UserCreateView(generic.CreateView):
    model = Users
    # fields = "__all__"
    fields = ["username", "password", "email"]
    template_name = "users/add.html"


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('auth:uindex'))
            else:
                return HttpResponse("The password is valid, but the account has been disabled!")
        else:
            return HttpResponse("The username and password were incorrect.")

    return render(request, "learn_django/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('auth:login'))
