import json, re, calendar
from datetime import date, timedelta

from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.db.models import Q

from utils.mixin_utils import LoginRequiredMixin
from rbac.models import Menu
from system.models import SystemSetup  # 网页标签等显示信息
from personal.forms import UserUpdateForm
from personal.models import WorkOrder

User = get_user_model()
# Create your views here.


class PersonalView(LoginRequiredMixin, View):
    """
    我的工作台
    """
    def get(self, request):
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        start_date = date.today().replace(day=1)
        _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
        end_date = start_date + timedelta(days_in_month)

        work_order = WorkOrder.objects.filter(Q(add_time__range=(start_date, end_date)),
                                              Q(proposer_id=request.user.id) |
                                              Q(receiver_id=request.user.id) |
                                              Q(approver_id=request.user.id))
        ret['work_order_1'] = work_order.filter(status='1').count()
        ret['work_order_2'] = work_order.filter(status="2").count()
        ret['work_order_3'] = work_order.filter(status="3").count()
        ret['work_order_4'] = work_order.filter(status="4").count()
        ret['start_date'] = start_date

        return render(request, 'personal/personal_index.html', ret)


class UserInfoView(LoginRequiredMixin, View):
    """
    个人中心：个人信息查看修改和修改
    """

    def get(self, request):
        return render(request, 'personal/userinfo/user_info.html')

    def post(self, request):
        ret = dict(status="fail")
        user = User.objects.get(id=request.POST['id'])
        user_update_form = UserUpdateForm(request.POST, instance=user)
        if user_update_form.is_valid():
            user_update_form.save()
            ret = {"status": "success"}
        return HttpResponse(json.dumps(ret), content_type='application/json')