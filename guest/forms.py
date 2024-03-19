from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Guest

class SignupForm(UserCreationForm):
    class Meta:
        model = Guest
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'phone_number',
            'email',
            'passport_serie',
            'password1', 
            'password2'
        ]

class LoginForm(AuthenticationForm):
    class Meta:
        model = Guest
   
