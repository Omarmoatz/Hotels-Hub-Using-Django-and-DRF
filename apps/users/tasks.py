from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.utils.html import strip_tags

from .models import User


@shared_task()
def get_users_count():
    """A pointless Celery task to demonstrate usage."""
    return User.objects.count()


@shared_task()
def send_email(subject, email, html_content):
    send_mail(
        subject=subject,
        message=strip_tags(html_content),
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        html_message=html_content
    )
