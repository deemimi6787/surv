from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    firstName = forms.CharField(max_length=30, required=True, help_text='Enter Your First Name')
    lastName = forms.CharField(max_length=30, required=True, help_text='Enter Your LastName')
    idno=forms.CharField(max_length=20,required=True,help_text="enter your id Number")
    phoneNo=forms.CharField(max_length=20,required=True,help_text="enter your phone Number")
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name','idno','phoneNo','email','username','password1', 'password2', )