# -*- coding: UTF-8 -*-
from models import Query
from rest_framework import serializers


class QuerySerializer(serializers.ModelSerializer):

    def validate_context(self, value):
        context = value.lower().split(' ')
        if 'select' not in context or 'from' not in context:
            raise serializers.ValidationError(
                "SQL Syntax Error: Query context ({0})".format(value))

        return value

    class Meta:
        model = Query
