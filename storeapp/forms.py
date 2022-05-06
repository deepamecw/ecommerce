import email
from logging import PlaceHolder
import re
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User

from django import forms


class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','PlaceHolder':'Enter Username'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','PlaceHolder':'Enter Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','PlaceHolder':'Enter password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','PlaceHolder':'Re-enter password'}))
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
   




       
          
        
   
  