# -*- coding: utf-8 -*-
from django.conf import settings
from condition.ventilation.models import Ventilation_Types, Ventilation_Products
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Template, context, RequestContext

def show_product(request, id):
    template_name = 'ventilation/product.html'
    return render_to_response(template_name, 
	{'product': Ventilation_Products.objects.get(pk=int(id)),
	},
	context_instance=RequestContext(request)
    )

def show_type(request, id):
    template_name = 'ventilation/type.html'
    return render_to_response(template_name,
        {'type': Ventilation_Types.objects.get(pk=int(id)),
	'products': Ventilation_Products.objects.filter(type_id=int(id)).order_by('-price'),
	},
        context_instance=RequestContext(request)
    )

def search(request):
    template_name = 'thermal/search.html'
    search = request.POST['search']
    type_id = int(request.POST['type_id'])
    if type_id:
	products = Ventilation_Products.objects.filter(types_id = type_id, name__icontains=search)
    else:
	products = Ventilation_Products.objects.filter(name__icontains=search)

    return render_to_response(template_name,
        {'products': products,},
        context_instance=RequestContext(request)
    )

