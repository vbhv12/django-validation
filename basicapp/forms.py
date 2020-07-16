from django import forms
from django.core import validators
from .models import *

def checkforz(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("please check")

class newuserform(forms.ModelForm):
    first_name=forms.CharField(validators=[checkforz])
    last_name=forms.CharField()
    email =forms.EmailField()
    
    class Meta:
        model=User
        fields='__all__'