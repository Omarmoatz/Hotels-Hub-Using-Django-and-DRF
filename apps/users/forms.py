from django import forms
from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.contrib.auth import forms as admin_forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm

from apps.users.models import User

class UserForm(UserCreationForm):
    
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
                'username',
                'email',
                'password1',
                'password2']
        

        
class ProfileForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter The Code',
                                                         'class':'form-control-lg w-100 border border-1'}))
    
    
class LoginForm(forms.Form):
    email = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder':'Enter Your Email',
                                                              'class':'form-control-lg w-100 border border-1'}))
    
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'Enter Your Password',
                                                                            'class':'form-control-lg w-100 border border-1'}))
class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):  # type: ignore[name-defined]
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):  # type: ignore[name-defined]
        model = User
        error_messages = {
            "username": {"unique": _("This username has already been taken.")},
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """
