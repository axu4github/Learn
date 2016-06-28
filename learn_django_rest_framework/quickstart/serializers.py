# -*- coding: UTF-8 -*-
from django.contrib.auth.models import User, Group
from models import Query
from rest_framework import serializers
from django.conf import settings


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('url', 'name')


# class QuerySerializer(serializers.Serializer):
#     context = serializers.CharField(
#         required=True, allow_blank=False, max_length=100)
#     created = serializers.DateTimeField(read_only=True)
#     language = serializers.ChoiceField(
#         choices=settings.LANGUAGE_CHOICES, default='sql')
#     formated = serializers.CharField(
#         allow_blank=False, max_length=1000, default='')  # 格式化后的查询内容
#     description = serializers.CharField(allow_blank=True, max_length=100)  # 查询描述
#     owner = serializers.CharField(allow_blank=False, max_length=30,
# default='')  # 执行/创建 人

class QuerySerializer(serializers.HyperlinkedModelSerializer):

    def validate_context(self, value):
        context = value.lower().split(' ')
        if 'select' not in context or 'from' not in context:
            raise serializers.ValidationError(
                "Query context ({0}) is not SQL Syntax".format(value))

        return value

    class Meta:
        model = Query
        fields = ('url', 'id', 'context', 'created', 'language',
                  'formated', 'description', 'owner')
