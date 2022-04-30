from users.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model= User
        fields= ["username","email","password1","password2"]

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )