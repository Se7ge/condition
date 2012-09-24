# -*- coding: utf-8 -*-
from django.conf import settings
from condition.catalog.models import Types, Producers, Products, Series
from django.http import HttpResponse, HttpResponseRedirect
#from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.template import Template, context, RequestContext
from django.contrib.flatpages.models import FlatPage

def show_catalog(request):
    template_name = 'catalog/catalog.html'
    return render_to_response(template_name, 
	{'producers': Producers.objects.all(), 
	'types': Types.objects.all(),},
        context_instance=RequestContext(request)
   )

def show_main(request):
    template_name = 'catalog/show_main.html'
    return render_to_response(template_name,
    	{'producers': Producers.objects.all(),
	'types': Types.objects.all(),
	'main_products': Products.objects.filter(show_in_main=True).order_by("-raiting")[0:12],
	'top_text': FlatPage.objects.get(pk=5),
        'bottom_text': FlatPage.objects.get(pk=6),},
	context_instance=RequestContext(request),
    )

def show_producer(request, id):
    template_name = 'catalog/producer.html'
    series = Series.objects.filter(producer_id = int(id))
    return render_to_response(template_name, 
	{'producer': Producers.objects.get(pk=int(id)),
	'producers': Producers.objects.all(),
        'types': Types.objects.all(),
	'producers_types': Types.objects.filter(pk__in=series.values_list('types_id', flat=True)),
	'series': series},
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
    series = Series.objects.select_related().filter(types_id = int(id))
    return render_to_response(template_name,
        {'producers': Producers.objects.all(),
	'types_producers': Producers.objects.filter(pk__in=series.values_list('producer_id', flat=True)),
	'types': Types.objects.all(),
        'type': Types.objects.get(pk=int(id)),
        'series': series},
        context_instance=RequestContext(request)
    )

def show_series(request, type_id, producer_id):
    template_name = 'catalog/series.html'
    return render_to_response(template_name, 
    	{'producer': Producers.objects.get(pk=int(producer_id)),
	'type': Types.objects.get(pk=int(type_id)),
	'producers': Producers.objects.all(),
	'types': Types.objects.all(),
	'series': Series.objects.select_related().filter(types_id=int(type_id), producer_id=int(producer_id)),
	'products': Products.objects.select_related().filter(series__types_id=int(type_id), series__producer_id=int(producer_id)),
	},
	context_instance=RequestContext(request)
    )

def search(request):
    template_name = 'catalog/search.html'
    search = request.POST['search']
    type_id = int(request.POST['type_id'])
    if type_id:
	products = Products.objects.select_related().filter(series__types_id = type_id, name__icontains=search)
    else:
	products = Products.objects.select_related().filter(name__icontains=search)

    return render_to_response(template_name,
        {'producers': Producers.objects.all(),
        'types': Types.objects.all(),
        'products': products,},
        context_instance=RequestContext(request)
    )

