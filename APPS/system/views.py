from django.shortcuts import render
from django.views.generic.base import View

from APPS.utils.mixin_utils import LoginRequiredMixin


# Create your views here.

class SystemView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'system/system_index.html')