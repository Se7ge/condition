# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('condition.catalog.views',
    url(r'^catalog/producer/(\d+)/$', 'show_producer'),
    url(r'^catalog/product/(\d+)/$', 'show_product'),
    url(r'catalog/types/(\d+)/$', 'show_type'),
    url(r'^catalog/$', 'show_catalog'),
)
