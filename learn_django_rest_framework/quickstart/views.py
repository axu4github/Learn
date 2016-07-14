# -*- coding: UTF-8 -*-
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView
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
    ---
    list:
        omit_serializer: true

    '''

    queryset = Query.objects.all()
    serializer_class = QuerySerializer


class StudyWithSwaggerApiView(CreateAPIView, ListAPIView, APIView):
    """
    ### 关于StudyWithSwaggerApiView的接口说明
    ***
    [官网地址](https://django-rest-swagger.readthedocs.io/en/latest/index.html) | [github](https://github.com/swagger-api/swagger-ui)

    * 如果安装[Markdown](https://pypi.python.org/pypi/Markdown)，注释中可以支持Markdown语法
    * 可以直接在Class的注释中定义方法的接口
    * 但是下面的get的例子没有成功，不知是不是因为`get`关键字的问题
    * 在QueryViewSet的Class注释中，针对list方法的注释是成功的
    ***
    ---
    # get:
    #     omit_serializer: true
    #     many: true

    """

    serializer_class = QuerySerializer

    def get(self, request):
        return Response("list function")

    def post(self, request):
        """
        重写CreateAPIView.post

        ---
        # type属性是显示在UI中的Model/Model Schema部分
        # type:
        #     cotext:
        #       description: SQL语句
        #       required: true
        #       type: string
        #     url:
        #       required: false
        #       type: url
        #     created_at:
        #       required: true
        #       type: string
        #       format: date-time

        # serializer: quickstart.serializers.QuerySerializer

        # 是否忽略serializer， 如果是false那么type或者parameters如果没有设置，则默认使用serializer
        omit_serializer: true
        many: true

        # parameters_strategy 选项：(replace/merge)
        parameters_strategy: replace

        # 未知，设置并没有起什么作用
        # omit_parameters:
        #     - query

        # 请求参数
        # parameters.paramType 常用有 query/from 两个选项
        # 1. query: 直接加到url后面：比如 http://example.com/whats-api/?parameter_name=parameter_context
        # 2. from: 表单请求的方式，加到请求的body中发送
        # 3. body: 未知
        parameters:
            - name: context
              description: SQL语句
              required: true
              type: string
              paramType: from
            # - name: other_foo
            #   paramType: query
            # - name: other_bar
            #   paramType: query
            # - name: avatar
            #   type: file

        # 返回状态说明（只是说明）
        responseMessages:
            - code: 400
              message: Bad Request
            - code: 401
              message: Not authenticated

        # 未知，设置并没有起什么作用
        # consumes:
        #     - application/json
        #     - application/xml

        # 请求参数格式 "Content-Type": "application/json"
        produces:
            - application/json
            - application/xml

        """

        print vars(request)
        print request.accepted_media_type
        print request.data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
