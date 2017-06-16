from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^users/$', views.UserIndexView.as_view(), name='uindex'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetailView.as_view(), name='udetail'),
]