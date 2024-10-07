from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.crypto import get_random_string
from model_utils.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _


class User(AbstractUser, TimeStampedModel):
    """
    Default custom user model for hotel-resrvation-system.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    username = models.CharField(
        _("username"),
        max_length=150,
        blank=True,
    )
    email = models.EmailField(
        max_length=300,
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )
    gender = models.CharField(max_length=200, choices=GENDER, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="profile", blank=True, null=True)

    country = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=600, blank=True)

    facebook = models.URLField(max_length=900, blank=True)
    twitter = models.URLField(max_length=900, blank=True)

    verified = models.BooleanField(default=False)

    code = models.CharField(max_length=200, blank=True)

    USERNAME_FIELD = "email"  # Change this line to specify the field for authentication
    REQUIRED_FIELDS = [
        "username",
    ]  # Add this line to specify the required fields for user creation

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.username or self.email

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = get_random_string(20)
        super().save(*args, **kwargs)

    def get_absolute_url(self) -> str:
        return reverse("users:detail", kwargs={"username": self.username})
