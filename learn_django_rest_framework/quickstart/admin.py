from django.contrib import admin
from models import Query

# Register your models here.


class QueryAdmin(admin.ModelAdmin):
    """docstring for QueryAdmin"""
    fields = ['context', 'language', 'description']
    list_display = ('id', 'context', 'language', 'created',
                    'formated', 'description', 'owner')
    list_filter = ['language']
    search_fields = ['context', 'language']

    def created(self):
        return "123 %s " % self.created

admin.site.register(Query, QueryAdmin)
