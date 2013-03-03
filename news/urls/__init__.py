# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('condition.news.views',
                       url(r'^news/(\d+)\.html$', 'show_news'),
                       url(r'^news/$', 'show_list'),
                       )
