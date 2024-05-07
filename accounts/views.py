from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.core.exceptions import ValidationError


from .models import User,Profile
from .forms import UserForm,ProfileForm


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