# -*- coding: utf-8 -*-
from django.conf import settings
from condition.prepared.models import Prepared
from django.shortcuts import render_to_response
from django.template import Template, context, RequestContext


def show_prepared(request, id):
    template_name = 'prepared/prepared.html'
    return render_to_response(template_name,
                              {'prepared_item': Prepared.objects.get(pk=int(id))},
                              context_instance=RequestContext(request))
