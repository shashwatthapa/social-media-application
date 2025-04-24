from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import Profilepic

class RegisterForm(UserCreationForm):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}))
    email = forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your email'}))
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}))
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}))
    class Meta:
        model = User 
        fields = ['username','email','password1','password2']

class ProfilepicForm(forms.ModelForm):
    class Meta:
        model = Profilepic
        fields = ['pic']

