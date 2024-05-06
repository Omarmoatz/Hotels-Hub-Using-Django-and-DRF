from django.shortcuts import render

from .models import User,Profile
from .forms import UserForm

def sign_up(request):
    form = UserForm(request.POST)

    return render(request, 'accounts/regester.html', {'form':form})
