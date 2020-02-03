import json

from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder

User = get_user_model()

from django.views.generic.base import View
from django.http import HttpResponse

from APPS.utils.mixin_utils import LoginRequiredMixin
from APPS.rbac.models import Role, Menu
from APPS.system.models import SystemSetup


class RoleView(LoginRequiredMixin, View):
    """
    角色管理
    """
    def get(self, request):
        ret = Menu.getMenuRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        return render(request, 'system/rbac/role-list.html', ret)