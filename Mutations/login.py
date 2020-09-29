from .models import Register
from django import forms

class UserLogin(forms.ModelForm):
    class Meta:
        model = Register
        fields = ["firstName","lastName","idNo","phoneNo","email","userName","password"]