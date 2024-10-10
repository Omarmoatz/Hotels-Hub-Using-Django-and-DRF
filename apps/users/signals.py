from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.users.models import User
from apps.hotel.models import Hotel


@receiver(post_save, sender=User)
def create_hotel(sender, instance, created, **kwargs):
    if instance.user_type == User.UserType.SELLER and created:
        Hotel.objects.create(
            user = instance,
            name = f"{instance.username} hotel",
            )
