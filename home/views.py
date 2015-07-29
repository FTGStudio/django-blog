from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template import RequestContext
import traceback
import sys
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    try:
        template_name = "home/index.html"

        def get_context_data(self, **kwargs):

            context = super(HomePageView, self).get_context_data(**kwargs)
            context['client_list'] = ""

            return context
    except Exception as inst:
        traceback.print_exc(file=sys.stdout)
        raise inst