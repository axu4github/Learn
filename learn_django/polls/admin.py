# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Choice, Question
from django.utils.translation import ugettext_lazy as _
from datetime import date


class ChoiceInline(admin.TabularInline):  # 输入框小空间占用
    # class ChoiceInline(admin.StackedInline): # 输入框大空间占用
    model = Choice
    extra = 3  # 默认显示添加几个


class PudateListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('pub_date')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'pub_date'

    def lookups(self, request, model_admin):
        """
        返回Filter可选的内容
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('2016', _('2016')),
            ('2017', _('2017')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value() == '2016':
            return queryset.filter(pub_date__year='2016')
        if self.value() == '2017':
            return queryset.filter(pub_date__year='2017')


class QuestionAdmin(admin.ModelAdmin):
    # 例1，普通顺序改变
    # fields = ['pub_date', 'question_text']

    # 例2，增加 header
    # fieldsets = [
    #     (None,               {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date']}),
    # ]

    # 例3，增加更多HTML标签以及效果
    fieldsets = [
        (
            None,
            {'fields': ['question_text']}
        ),
        (
            'Date information',
            {'fields': ['pub_date'], 'classes': ['collapse']}
        ),
    ]

    # 将关联类添加到Admin中
    inlines = [ChoiceInline]

    # List页面显示内容
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # List页面哪些列可以跳转到更新页面，默认是第一列
    list_display_links = ('pub_date', ) #这么设置以后第二列也可以跳转到修改页面。
    # list_display_links = None  # 禁止点击跳转到更新页面
    # 页面中可以编辑
    # list_editable = ['question_text', 'pub_date']
    list_editable = ['question_text']
    # 过滤器
    list_filter = ['pub_date', PudateListFilter]

    # 搜索框
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
