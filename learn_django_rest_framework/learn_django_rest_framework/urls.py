"""learn_django_rest_framework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
# from rest_framework.urlpatterns import format_suffix_patterns
from quickstart import views

router = routers.DefaultRouter()
router.register(r'queryviewset', views.QueryViewSet)

query4viewset = views.QueryViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^query/', views.query, name='query'),
    url(r'^query4view/', views.QueryView.as_view(), name='query4view'),
    url(r'^query4mixinview/', views.QueryMixinView.as_view(), name='query4mixinview'),
    url(r'^query4viewset/', query4viewset, name='query4viewset'),
    url(r'^studyswagger/', views.StudyWithSwaggerApiView.as_view(), name='studyswagger'),
]
