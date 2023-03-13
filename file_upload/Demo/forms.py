from django import forms
from .models import *

class demo_form(forms.ModelForm):
    class Meta:
        model = Demo_Models
        fields = ['name','email','profile_pic']
