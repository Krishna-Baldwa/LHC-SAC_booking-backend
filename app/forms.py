from django import forms
from .models import FormRequest

class FormRequestForm(forms.ModelForm):
    class Meta:
        model =FormRequest
        fields = ['contact','reason','council','starttime','endtime','room']
