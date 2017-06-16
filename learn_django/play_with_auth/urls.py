from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^users/$', login_required(views.UserIndexView.as_view()), name='uindex'),
    url(r'^users/(?P<pk>[0-9]+)/$', login_required(views.UserDetailView.as_view()), name='udetail'),
    url(r'^users/add/$', views.UserCreateView.as_view(), name='uadd'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
]
