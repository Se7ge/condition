# -*- coding: utf-8 -*-
from django.conf import settings
from condition.services.models import Services
from django.shortcuts import render_to_response
from django.template import Template, context, RequestContext

def show_service(request, id):
    template_name = 'services/service.html'
    return render_to_response(template_name,
	{'service': Services.objects.get(pk=int(id)),
    	},
    	context_instance=RequestContext(request)
    )
