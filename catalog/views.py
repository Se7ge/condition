# -*- coding: utf-8 -*-
from django.conf import settings
from condition.catalog.models import Types, Producers, Products
from django.http import HttpResponse, HttpResponseRedirect
#from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.template import Template, context, RequestContext

def show_catalog(request):
    template_name = 'catalog/catalog.html'
    return render_to_response(template_name, 
	{'producers': Producers.objects.all(), 
	'types': Types.objects.all(),},
        context_instance=RequestContext(request)
   )

def show_producer(request, id):
    template_name = 'catalog/producer.html'
    return render_to_response(template_name, 
	{'producer': Producers.objects.get(pk=int(id)),
	'producers': Producers.objects.all(),
        'types': Types.objects.all(), 
	'products': Products.objects.filter(producer_id = int(id))},
        context_instance=RequestContext(request)
    )

def show_product(request, id):
    template_name = 'catalog/product.html'
    return render_to_response(template_name, 
	{'product': Products.objects.get(pk=int(id)),
	'producers': Producers.objects.all(),
	'types': Types.objects.all(),},
	context_instance=RequestContext(request)
    )

def show_type(request, id):
    template_name = 'catalog/type.html'
    return render_to_response(template_name,
        {'producers': Producers.objects.all(),
	'types': Types.objects.all(),
        'type': Types.objects.get(pk=int(id)),
        'products': Products.objects.filter(type_id = int(id))},
        context_instance=RequestContext(request)
    )
