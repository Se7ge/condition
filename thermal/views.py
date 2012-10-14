# -*- coding: utf-8 -*-
from django.conf import settings
from condition.thermal.models import Thermal_Types, Thermal_Producers, Thermal_Products
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Template, context, RequestContext

def show_product(request, id):
    template_name = 'thermal/product.html'
    return render_to_response(template_name, 
	{'product': Thermal_Products.objects.get(pk=int(id)),
	},
	context_instance=RequestContext(request)
    )

def show_type(request, id):
    template_name = 'thermal/type.html'
    products = Thermal_Products.objects.select_related().filter(type_id = int(id))
    return render_to_response(template_name,
        {'types_producers': Thermal_Producers.objects.filter(pk__in=products.values_list('producer_id', flat=True)),
        'type': Thermal_Types.objects.get(pk=int(id)),
	},
        context_instance=RequestContext(request)
    )

def show_products(request, type_id, producer_id):
    template_name = 'thermal/products.html'
    return render_to_response(template_name, 
    	{'producer':Thermal_Producers.objects.get(pk=int(producer_id)),
	'type': Thermal_Types.objects.get(pk=int(type_id)),
	'products': Thermal_Products.objects.filter(type_id=int(type_id), producer=int(producer_id)).order_by('-price'),
	},
	context_instance=RequestContext(request)
    )

def search(request):
    template_name = 'thermal/search.html'
    search = request.POST['search']
    type_id = int(request.POST['type_id'])
    if type_id:
	products = Thermal_Products.objects.filter(types_id = type_id, name__icontains=search)
    else:
	products = Thermal_Products.objects.filter(name__icontains=search)

    return render_to_response(template_name,
        {'products': products,},
        context_instance=RequestContext(request)
    )

