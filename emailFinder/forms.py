# forms.py
from django import forms
from .models import WebsiteModel

class MultipleEmailsForm(forms.ModelForm):
    class Meta:
        model = WebsiteModel
        fields = ['email_list']

