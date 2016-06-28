from django.contrib import admin
from models import Query

# Register your models here.

class QueryAdmin(admin.ModelAdmin):
    """docstring for QueryAdmin"""
    # fields = ['context', 'language']
    list_display = ('context', 'language', 'created')
        
admin.site.register(Query, QueryAdmin)
