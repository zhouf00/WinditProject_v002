import json, re, calendar
from datetime import date, timedelta

from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.db.models import Q

from APPS.utils.mixin_utils import LoginRequiredMixin
from APPS.rbac.models import Menu
from APPS.system.models import SystemSetup  # 网页标签等显示信息
from APPS.personal.models import WorkOrder

# Create your views here.


class PersonalView(LoginRequiredMixin, View):
    """
    我的工作台
    """
    def get(self, request):
        ret = Menu.getMenuRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        start_date = date.today().replace(day=1)
        _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
        end_date = start_date + timedelta(days_in_month)

        work_order = WorkOrder.objects.filter()
        ret['work_order_1'] = work_order.filter(status='1').count()