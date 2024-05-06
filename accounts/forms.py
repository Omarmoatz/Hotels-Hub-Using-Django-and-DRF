from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

class UserForm(UserCreationForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Your Full Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Your username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Your email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm The password'}))
    class Meta:
        model = User
        fields = [
                'full_name',
                'username',
                'email',
                'password1',
                'password2']