# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('condition.thermal.views',
    url(r'^thermal/(\d+)/(\d+)/$', 'show_products'),
    url(r'^thermal/product/(\d+)/$', 'show_product'),
    url(r'^thermal/types/(\d+)/$', 'show_type'),
    url(r'^thermal/search/$', 'search'),
)

