from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^name/$', views.name, name='name'),
    url(r'^contact/$', views.contact, name='contact'),
]