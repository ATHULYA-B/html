from django import forms
from .models import *

class Empform(forms.ModelForm):
    class Meta:
        model=Emp
        fields='__all__'