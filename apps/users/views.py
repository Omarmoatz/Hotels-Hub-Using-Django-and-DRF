from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.db.models import QuerySet
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView

from apps.users.forms import LoginForm
from apps.users.forms import ProfileForm
from apps.users.forms import UserForm
from apps.users.models import User


def sign_up(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]  # to send him the activation mail

            user_form = form.save(commit=False)
            user_form.is_active = False
            user_form.save()

            user = User.objects.get(username=username)
            send_mail(
                "Your Activation Mail",  # subject
                f"Use this code {user.code} to activate your account",  # body
                settings.EMAIL_BACKEND,  # from
                (email,),  # to
            )

            return redirect(f"/users/activate/{username}")

    else:
        form = UserForm()
    return render(request, "users/register.html", {"form": form})


def activate(request, username):
    user = User.objects.get(username=username)
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            input_Code = form.cleaned_data["code"]
            if input_Code == user.code:
                user.code = ""
                user.is_active = True
                user.save()
                messages.success(request, "Your Account is Activated You Can Now Login")
                return redirect("/users/login")
            error = "Invalid activation code"
            return render(
                request, "users/activation.html", {"form": form, "error": error}
            )
    else:
        form = ProfileForm()
    return render(request, "users/activation.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                messages.success(request, f"Hey {user}, Welcome Back")
                return redirect("/")
            if User.objects.filter(email=email).exists():
                messages.error(request, "Invalid Password.")

            else:
                messages.error(request, "Invalid Email.")

                #     # Check if the username is incorrect
                # user_by_username = authenticate(username=username, password='')
                # if user_by_username is None:
                #     messages.error(request, 'Invalid username.')
                # else:
                #     # Check if the password is incorrect
                #     messages.error(request, 'Invalid password.')
    else:
        form = LoginForm()

    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("/")


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self) -> str:
        assert self.request.user.is_authenticated  # type guard
        return self.request.user.get_absolute_url()

    def get_object(self, queryset: QuerySet | None = None) -> User:
        assert self.request.user.is_authenticated  # type guard
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self) -> str:
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()
