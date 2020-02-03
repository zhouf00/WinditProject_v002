from django.shortcuts import render
from django.views.generic import TemplateView

from .mixin import LoginRequiredMixin
from APPS.custom import BreadcrumbMixin


# Create your views here.

class SystemView(LoginRequiredMixin, BreadcrumbMixin, TemplateView):

    template_name = 'system/system_index.html'
