from django import forms
from APPS.system.models import SystemSetup


class SystemSetupForm(forms.ModelForm):
    class Meta:
        model = SystemSetup
        fields = '__all__'