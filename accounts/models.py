from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string


GENDER = (
    ('Male','Male'),
    ('Female', 'Female')
)

class User(AbstractUser):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=300, unique=True)

    gender = models.CharField(max_length=200, choices=GENDER, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField( upload_to='profile' ,blank=True, null=True)

    country = models.CharField( max_length=200 ,blank=True, null=True)
    address = models.CharField( max_length=600 ,blank=True, null=True)

    facebook = models.URLField( max_length=900, blank=True, null=True)
    twitter = models.URLField( max_length=900, blank=True, null=True)

    verified = models.BooleanField(default=False)
    created_at = models.DateField( auto_now=True)

    code = models.CharField( max_length=200 , blank=True, null=True)

    USERNAME_FIELD = "email"  # Change this line to specify the field for authentication
    EMAIL_FIELD = "email"  # Add this line to specify the email field for authentication
    REQUIRED_FIELDS = ['username']  # Add this line to specify the required fields for user creation

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.username or self.email
    
    def save(self, *args, **kwargs):
       self.code = get_random_string(20)
       super().save(*args, **kwargs) 