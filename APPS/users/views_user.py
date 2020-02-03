import json, re

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

User = get_user_model()

from django.views.generic.base import View
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.core.serializers.json import DjangoJSONEncoder

from APPS.users.forms import LoginForm
from APPS.utils.mixin_utils import LoginRequiredMixin
from APPS.system.models import SystemSetup


class UserBackend(ModelBackend):
    """
    自定义用户验证: setting中对应配置
    AUTHENTICATION_BACKENDS = (
        'users.views.UserBackend',
        )
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user =User.objects.get(Q(username=username)|Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class IndexView(LoginRequiredMixin, View):
    """
    工作台主页
    """
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'personal/personal_index.html')
        else:
            return HttpResponse('失败')
    #     return HttpResponseRedirect('/personal/')


class LoginView(View):
    """
    用户登录认证，通过form表单进行输入合规验证
    """
    def get(self, request):
        if not request.user.is_authenticated:
            ret = (SystemSetup.getSystemSetupLastData())
            return render(request, 'system/users/login.html', ret)
        else:
            return HttpResponse('登陆失败')

    def post(self, request):
        redirect_to = request.GET.get('next', '/index/')
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(redirect_to)
                else:
                    msg = '用户未激活'
                    ret = {'msg': msg, 'login_form':login_form}
                    return render(request, 'system/users/login.html', ret)
            else:
                msg = '用户名或密码错误'
                ret = {'msg':msg, 'login_form':login_form}
                return render(request, 'system/users/login.html', ret)
        else:
            msg = '用户名或密码不能够为空'
            ret = {'msg':msg, 'login_form':login_form}
            return render(request, 'system/users/login.html', ret)


class LogoutView(View):
    """
    用户登出
    """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))


class UserView(LoginRequiredMixin, View):
    """
    用户管理
    """
    def get(self, request):
        ret = SystemSetup.getSystemSetupLastData()
        return render(request, 'system/users/user-list.html')


class UserListView(LoginRequiredMixin, View):
    """
    获取用户列表信息
    """
    def get(self, request):
        fields = ['id', 'name', 'gender', 'mobile', 'email', 'department__title', 'post', 'superior__name', 'is_active']
        filters = dict()
        if 'select' in request.GET and request.GET.get('select'):
            filters['is_active'] = request.GET.get('select')
        ret = dict(data=list(User.objects.filter(**filters).values(*fields).exclude(username='admin')))
        return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')