from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string
from django.db.models.signals import post_save
from django.dispatch import receiver


GENDER = (
    ('Male','Male'),
    ('Female', 'Female')
)

class User(AbstractUser):
    full_name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=300, unique=True)
    gender = models.CharField(max_length=200, choices=GENDER, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)

    # USERNAME_FIELD : to make the user login with what i want 
    USERNAME_FIELD = "email"  # Change this line to specify the field for authentication
    EMAIL_FIELD = "email"  # Add this line to specify the email field for authentication
    REQUIRED_FIELDS = ['username']  # Add this line to specify the required fields for user creation

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    image = models.ImageField( upload_to='profile' ,blank=True, null=True)

    country = models.CharField( max_length=200 ,blank=True, null=True)
    address = models.CharField( max_length=600 ,blank=True, null=True)

    facebook = models.URLField( max_length=900, blank=True, null=True)
    twitter = models.URLField( max_length=900, blank=True, null=True)

    verified = models.BooleanField(default=False)
    created_at = models.DateField( auto_now_add=True)

    code = models.CharField( max_length=200 , default=get_random_string(20), blank=True, null=True)

    def __str__(self):
        return str(self.user)
    
    class Meta:
        ordering = ['-created_at']
    
@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(
            user=instance,
        )

    
    

