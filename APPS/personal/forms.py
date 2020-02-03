from django import forms
from django.contrib.auth import get_user_model

from APPS.personal.models import WorkOrder, WorkOrderRecord

User = get_user_model()


class ImageUploadForm(forms.ModelForm):
    # class Meta:
    #     model = User
    #     fields = ['image']
    pass


class UserUpdateForm(forms.ModelForm):
    # class Meta:
    #     model = User
    #     fields = ['name', 'gender', 'birthday', 'email']
    pass