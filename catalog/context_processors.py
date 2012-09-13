# -*- coding: utf-8 -*-
from django.conf import settings
from condition.catalog.models import Types, Producers, Products 

def get_settings(request):
    return {'STATIC_URL': settings.STATIC_URL,}

def show_catalog(request):
    template_name = 'catalog/catalog.html'
    return {'producers': Producers.objects.all(),
        'types': Types.objects.all(),}

