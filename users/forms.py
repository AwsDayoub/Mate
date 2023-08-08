from dataclasses import field
from django.forms import ModelForm
from .models import CustomUser
from django import forms

class RegisterForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username","email","password","image","status","collage","level"]

class LogInForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)