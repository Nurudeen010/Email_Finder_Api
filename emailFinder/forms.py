# forms.py
from django import forms
from .models import FinderModel

class MultipleEmailsForm(forms.ModelForm):
    class Meta:
        model = FinderModel
        fields = ['web_list', 'emails']

