from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Guest

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Guest
        fields = '__all__'

class LoginForm(AuthenticationForm):
    class Meta:
        model = Guest