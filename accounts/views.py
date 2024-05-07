from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import User,Profile
from .forms import UserForm,ProfileForm,LoginForm


def sign_up(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
           
            user_form = form.save(commit=False)
            user_form.is_active = False 
            user_form.save()

            profile = Profile.objects.get(user__username=username)
            send_mail(
                'Your Activation Mail',
                f'Use this code {profile.code} to activate your account',
                'omar@gmail.com',
                [settings.EMAIL_BACKEND]
            )

            return redirect(f'/accounts/activate/{username}')
             
    else:
        form =UserForm()
    return render(request, 'accounts/regester.html', {'form':form})


def activate(request,username):
    profile = Profile.objects.get(user__username=username)
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            code = profile.code
            input_Code = form.cleaned_data['code']
            if input_Code == code: 
                code = ''
                profile.user.is_active = True
                profile.save()
                profile.user.save()
                return redirect('/')
            else:
                error = 'Invalid activation code'
                return render(request, 'accounts/activation.html', {'form': form, 'error': error})
    else:
        form = ProfileForm()
    return render(request, 'accounts/activation.html', {'form':form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Invalid Password.')
                    
                 
                else:
                    messages.error(request, 'Invalid Email.')
                    
                #     # Check if the username is incorrect
                # user_by_username = authenticate(username=username, password='')
                # if user_by_username is None:
                #     messages.error(request, 'Invalid username.')
                # else:
                #     # Check if the password is incorrect
                #     messages.error(request, 'Invalid password.')

    else:
        form =LoginForm()

    return render(request, 'accounts/login.html', {'form':form})