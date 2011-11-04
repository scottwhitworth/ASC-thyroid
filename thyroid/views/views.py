from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django import forms
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import simplejson
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView

from thyroid.models import Diagnosis, Category, Reference

import logging
logger = logging.getLogger(__name__)

class HomeView(TemplateView):
    template_name = 'thyroid/home.html'

def diagnosis_list(request, template='thyroid/diagnosis_list.html'):
    logger.debug('diagnosis_list')
    diagnoses = Diagnosis.objects.select_related().order_by('category__order')
    context = {'diagnoses': diagnoses}
    return render_to_response(template, context,
            context_instance=RequestContext(request))

def diagnosis(request, d_id, template='thyroid/diagnosis.html'):
    try:
        diagnosis = Diagnosis.objects.select_related('reference').get(
                    pk=d_id)
    except Diagnosis.DoesNotExist:
        return Http404
    context = {'diagnosis': diagnosis}
    return render_to_response(template, context, 
            context_instance=RequestContext(request))
