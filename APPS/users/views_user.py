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
            return render(request, 'index.html')
        else:
            return HttpResponse('失败')
        # return HttpResponseRedirect('/personal/')


class LoginView(View):
    """
    用户登录认证，通过form表单进行输入合规验证
    """
    def get(self, request):
        if not request.user.is_authenticated:
            ret = (SystemSetup.getSystemSetupLastData())
            return render(request, 'system/users/login.html')
        else:
            return HttpResponse('登陆失败')

    def post(self, request):
        redirect_to = request.GET.get('next', '/index')
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
                    return render(request, 'system/users/login.html')
            else:
                msg = '用户名或密码错误'
                ret = {'msg':msg, 'login_form':login_form}
                return render(request, 'system/users/login.html')
        else:
            msg = '用户名或密码不能够为空'
            ret = {'msg':msg, 'login_form':login_form}
            return render(request, 'system/users/login.html')


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