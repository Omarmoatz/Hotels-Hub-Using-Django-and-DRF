from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User,Profile

class UserForm(UserCreationForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Your Full Name',
                                                              'class':'form-control-lg w-100 border border-1'}))
    
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Your username',
                                                             'class':'form-control-lg w-100 border border-1 '}))
    
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Your email',
                                                          'class':'form-control-lg w-100 border border-1'}))
    

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Your password',
                                                                  'class':'form-control-lg w-100 border border-1'}))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm The password',
                                                                  'class':'form-control-lg w-100 border border-1'}))
    
    class Meta:
        model = User
        fields = [
                'full_name',
                'username',
                'email',
                'password1',
                'password2']
        

        
class ProfileForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter The Code',
                                                         'class':'form-control-lg w-100 border border-1'}))
    
    
class LoginForm(forms.Form):
    email = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder':'Enter Your Username or Email',
                                                              'class':'form-control-lg w-100 border border-1'}))
    
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'Enter Your Password',
                                                                            'class':'form-control-lg w-100 border border-1'}))