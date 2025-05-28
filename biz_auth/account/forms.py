from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import User
from django.core import validators

class SigninForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))

class SignupForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': "form-control"}))


class UserRegisterForm(forms.ModelForm):
    otp_code = forms.CharField(required=True ,label='OTP code', widget=forms.TextInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['otp_code', 'email', 'full_name', 'username', 'password1', 'password2']


