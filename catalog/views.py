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
        'products': Products.objects.select_related().filter(type_id = int(id))},
        context_instance=RequestContext(request)
    )

def search(request):
    template_name = 'catalog/search.html'
    search = request.POST['search']
    type_id = int(request.POST['type_id'])
    if type_id:
	products = Products.objects.select_related().filter(type_id = type_id, name__icontains=search)
    else:
	products = Products.objects.select_related().filter(name__icontains=search)

    return render_to_response(template_name,
        {'producers': Producers.objects.all(),
        'types': Types.objects.all(),
        'products': products,},
        context_instance=RequestContext(request)
    )

