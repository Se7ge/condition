# -*- coding: utf-8 -*-
from django.conf import settings
from condition.catalog.models import Types, Producers, Products
from condition.thermal.models import Thermal_Types
from condition.purifier.models import Purifier_Types
from condition.ventilation.models import Ventilation_Types
from condition.services.models import Services
from condition.prepared.models import Prepared


def get_settings(request):
    return {'STATIC_URL': settings.STATIC_URL, }


def show_catalog(request):
#    template_name = 'catalog/catalog.html'
    return {'producers': Producers.objects.all(),
            'types': Types.objects.all(),
            'thermal_types': Thermal_Types.objects.all(),
            'purifier_types': Purifier_Types.objects.all(),
            'ventilation_types': Ventilation_Types.objects.all(),
            'services': Services.objects.all(),
            'prepared': Prepared.objects.all(),
            }

