# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('condition.ventilation.views',
    url(r'^ventilation/product/(\d+)/$', 'show_product'),
    url(r'^ventilation/types/(\d+)/$', 'show_type'),
    url(r'^ventilation/search/$', 'search'),
)

