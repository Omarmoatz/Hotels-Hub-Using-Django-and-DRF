from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.crypto import get_random_string
from model_utils.models import TimeStampedModel


class User(AbstractUser, TimeStampedModel):
    """
    Default custom user model for hotel-resrvation-system.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """
    GENDER = (
        ('Male','Male'),
        ('Female', 'Female')
    )
    # First and last name do not cover name patterns around the globe
    email = models.EmailField(max_length=300, unique=True)
    gender = models.CharField(max_length=200, choices=GENDER, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField( upload_to='profile' ,blank=True, null=True)

    country = models.CharField( max_length=200 ,blank=True, null=True)
    address = models.CharField( max_length=600 ,blank=True, null=True)

    facebook = models.URLField( max_length=900, blank=True, null=True)
    twitter = models.URLField( max_length=900, blank=True, null=True)

    verified = models.BooleanField(default=False)

    code = models.CharField( max_length=200 , blank=True)

    USERNAME_FIELD = "email"  # Change this line to specify the field for authentication
    REQUIRED_FIELDS = ['username']  # Add this line to specify the required fields for user creation

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.username or self.email
    
    def save(self, *args, **kwargs):
        if not self.code:
            self.code = get_random_string(20)
        super().save(*args, **kwargs) 

    def get_absolute_url(self) -> str:
        return reverse("users:detail", kwargs={"username": self.username})
  