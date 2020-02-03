import re, json

from django.shortcuts import render, HttpResponse
from django.views.generic.base import View, TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model, login, logout
from django.urls import reverse

from .mixin import LoginRequiredMixin
# from apps.custom import BreadcrumbMixin


User = get_user_model()


class IndexView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'index.html')


# 登陆
class LoginView(View):

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, '')
        else:
            return HttpResponseRedirect('/')

    def post(self, request):
        return render(request,'')


# 登出
class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))


class UserView(LoginRequiredMixin, BreadcrumbMixin, TemplateView):
    template_name = 'user.html'


# 获取用户信息列表
class UserListView(LoginRequiredMixin, View):

    def get(self, request):
        pass