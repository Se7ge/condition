from django.conf import settings
from condition.catalog.models import Types, Producers, Products 

def get_settings(context):
    return {'STATIC_URL': settings.STATIC_URL}

def show_catalog(request):
    template_name = 'catalog/catalog.html'
    return {'producers': Producers.objects.all(),
        'types': Types.objects.all(),}

