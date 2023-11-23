from django import forms
from App1.models import*
class Empform(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'