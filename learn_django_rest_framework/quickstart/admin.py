from django.contrib import admin
from models import Query

# Register your models here.


@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    """docstring for QueryAdmin"""
    fields = ['context']
    list_display = ('id', 'context', 'language', 'created',
                    'formated', 'description', 'owner')
    list_filter = ['language']
    search_fields = ['context', 'language']
