from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.core.exceptions import ValidationError


from .models import User,Profile
from .forms import UserForm


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

            return redirect(f'accounts/activate/{username}')
             
    else:
        form =UserForm()
    return render(request, 'accounts/regester.html', {'form':form})
