# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('condition.prepared.views',
    url(r'^prepared/(\d+)/$', 'show_prepared'),
)

