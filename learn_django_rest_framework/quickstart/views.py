# -*- coding: UTF-8 -*-
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from quickstart.serializers import QuerySerializer
from models import Query
import sqlparse


@api_view(['GET'])
def query(request, format=None):
    '''
    Django-Rest-Framework Function Based Views

    url => http://127.0.0.1:8000/query/?context=%27select%20*%20from%20a%27
    '''
    requestData = {'context': 'select * from a'}
    serializer = QuerySerializer(data=requestData)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QueryView(APIView):
    '''
    Django-Rest-Framework Class Based Views (未使用Mixin)
    '''

    def post(self, request, format=None):
        requestData = {'context': request.data}
        print request.data
        serializer = QuerySerializer(data=requestData)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QueryMixinView(CreateAPIView):
    '''
    Django-Rest-Framework Class Based Views (使用Mixin)

    和上面未继承Mixin的方式区别于：
    1. 继承不同的Mixin类可以直接获取到已经定义好的方法。

    比如本例继承了CreateAPIView，那么直接就会有post的方法可以使用，不用在自己完成post方法

    具体可以继承的APIView可以去rest_framework.generics找
    '''

    serializer_class = QuerySerializer


class QueryViewSet(viewsets.ModelViewSet):
    '''
    Django-Rest-Framework Class Based Views (使用ViewSet)

    和上面继承Mixin的方式区别于：
    1. 如果继承ViewSet那么可以获取一组接口，具体可以去rest_framework.viewsets查看
    2. 可以使用rest_framework.routers控制url

    需要指定：
    1. queryset
    2. serializer_class

    '''

    queryset = Query.objects.all()
    serializer_class = QuerySerializer
