import re

from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

# from APPS.users.models import Structure

class LoginForm(forms.Form):
    username = forms.CharField(required=True, error_messages={"required": u"请填写用户名"})
    password = forms.CharField(required=True, error_messages={"required": u"请填写密码"})