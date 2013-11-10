# -*- coding: utf-8 -*-
from django.conf import settings
from condition.purifier.models import Purifier_Types, Purifier_Producers, Purifier_Products
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Template, context, RequestContext


def show_product(request, id):
    template_name = 'purifier/product.html'
    return render_to_response(template_name,
                              {'product': Purifier_Products.objects.get(pk=int(id)), },
                              context_instance=RequestContext(request))


def show_type(request, id):
    template_name = 'purifier/type.html'
    products = Purifier_Products.objects.select_related().filter(type_id = int(id))
    return render_to_response(template_name,
                              {'types_producers': Purifier_Producers.objects.filter(
                                  pk__in=products.values_list('producer_id', flat=True)),
                               'type': Purifier_Types.objects.get(pk=int(id)), },
                              context_instance=RequestContext(request))


def show_products(request, type_id, producer_id):
    template_name = 'purifier/products.html'
    return render_to_response(template_name,
                              {'producer':Purifier_Producers.objects.get(pk=int(producer_id)),
                               'type': Purifier_Types.objects.get(pk=int(type_id)),
                               'products': Purifier_Products.objects.filter(
                                   type_id=int(type_id), producer=int(producer_id)).order_by('-price'), },
                              context_instance=RequestContext(request))


def search(request):
    template_name = 'purifier/search.html'
    search = request.POST['search']
    type_id = int(request.POST['type_id'])
    if type_id:
        products = Purifier_Products.objects.filter(types_id=type_id, name__icontains=search)
    else:
        products = Purifier_Products.objects.filter(name__icontains=search)

    return render_to_response(template_name,
                              {'products': products},
                              context_instance=RequestContext(request))

