# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('condition.purifier.views',
                       url(r'^purifier/(\d+)/(\d+)/$', 'show_products'),
                       url(r'^purifier/product/(\d+)/$', 'show_product'),
                       url(r'^purifier/types/(\d+)/$', 'show_type'),
                       url(r'^purifier/search/$', 'search'),
)

