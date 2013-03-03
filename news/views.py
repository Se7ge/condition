# -*- coding: utf-8 -*-
from django.conf import settings
from condition.news.models import News
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Template, context, RequestContext


def show_list(request):
    template_name = 'news/list.html'
    return render_to_response(template_name,
                              {'news_list': News.objects.filter(active=True).all(), 'page_title': u"Обзоры",},
                              context_instance=RequestContext(request))


def show_news(request, id):
    template_name = 'news/news.html'
    news = News.objects.get(pk=int(id))
    return render_to_response(template_name,
                              {'news': news, 'page_title': news.title},
                              context_instance=RequestContext(request))