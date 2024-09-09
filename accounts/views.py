from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages

from .models import User
from .forms import UserForm,ProfileForm,LoginForm


def sign_up(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email'] # to send him the activation mail
           
            user_form = form.save(commit=False)
            user_form.is_active = False 
            user_form.save()

            user = User.objects.get(username=username)
            send_mail(
                'Your Activation Mail',
                f'Use this code {user.code} to activate your account',
                'omar@gmail.com',
                [settings.EMAIL_BACKEND]
            )
            
            return redirect(f'/accounts/activate/{username}')
             
    else:
        form =UserForm()
    return render(request, 'accounts/register.html', {'form':form})


def activate(request,username):
    user = User.objects.get(user__username=username)
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            input_Code = form.cleaned_data['code']
            if input_Code == user.code: 
                user.code = ''
                user.is_active = True
                user.save()
                messages.success(request, 'Your Account is Activated You Can Now Login')
                return redirect('accounts:login')
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
            if user:
                login(request, user)
                messages.success(request, f'Hey {user}, Welcome Back')
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


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('/')