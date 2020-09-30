from .models import Mutation
from django import forms

class MutationEntry(forms.ModelForm):
    class Meta:
        model = Mutation
        fields = ["emp","county","location","idNumber"]