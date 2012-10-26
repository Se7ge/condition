# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('condition.services.views',
    url(r'^services/(\d+)/$', 'show_service'),
)

