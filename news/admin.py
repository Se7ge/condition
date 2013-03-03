# -*- coding: utf-8 -*-
from django.contrib import admin
from condition.news.models import News


class NewsAdmin(admin.ModelAdmin):
    fields = ('title', 'brief', 'description', 'active')

admin.site.register(News, NewsAdmin)
