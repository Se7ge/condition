# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('condition.catalog.views',
    url(r'^catalog/producer/(\d+)/$', 'show_producer'),
    url(r'^catalog/product/(\d+)/$', 'show_product'),
    url(r'^catalog/types/(\d+)/$', 'show_type'),
    url(r'^catalog/(\d+)/(\d+)/$', 'show_series'),
    url(r'^catalog/search/result/$', 'search'),
    url(r'^catalog/search/', 'search_form'),
    url(r'^catalog/$', 'show_catalog'),
    url(r'^$','show_main'),
)
