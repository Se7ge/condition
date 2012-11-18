# -*- coding: utf-8 -*-
from django.conf import settings
from condition.catalog.models import Types, Producers, Products, Series
from django.http import HttpResponse, HttpResponseRedirect
#from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.template import Template, context, RequestContext
from django.contrib.flatpages.models import FlatPage
from django.db.models import Max, Min

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
        'bottom_text': FlatPage.objects.get(pk=6),
        'favorite_text': FlatPage.objects.get(pk=9),
        },
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
        'products': Products.objects.select_related().filter(series__types_id=int(type_id), series__producer_id=int(producer_id)).order_by('series__ordernum','series__name', 'price'),
        },
        context_instance=RequestContext(request)
    )

def search(request):
    template_name = 'catalog/search_result.html'
    where = {}
    type_id = int(request.POST['type_id'])

    if type_id:
        _type = Types.objects.get(pk=int(type_id))
        where['series__types_id'] = type_id
    else:
        _type = {}

    where['name__icontains'] = request.POST['search']

    if 'extended' in request.POST and request.POST['extended']:
        producer_id = int(request.POST['producer_id'])
        if producer_id:
            where['series__producer_id'] = int(request.POST['producer_id'])
        where['price__gte'] = float(request.POST['price_from'])
        where['price__lte'] = float(request.POST['price_to'])
        where['area__gte'] = float(request.POST['area_from'])
        where['area__lte'] = float(request.POST['area_to'])

    products = Products.objects.select_related().filter(**where)

    return render_to_response(template_name,
        {'producers': Producers.objects.all(),
        'types': Types.objects.all(),
	    'type': _type,
        'products': products,},
        context_instance=RequestContext(request)
    )

def search_form(request):
    template_name = 'catalog/search.html'
    return render_to_response(template_name, 
        {'types': Types.objects.all(),
        'producers': Producers.objects.all(),
        'min_price': float(Products.objects.all().aggregate(Min('price'))['price__min']),
        'max_price': float(Products.objects.all().aggregate(Max('price'))['price__max']),
        'min_area': float(Products.objects.all().aggregate(Min('area'))['area__min']),
        'max_area': float(Products.objects.all().aggregate(Max('area'))['area__max']),
        },
        context_instance=RequestContext(request)
    )
