from django.core.exceptions import ValidationError
from django.db import models
from model_utils.models import TimeStampedModel


class MainSettings(TimeStampedModel):
    name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to="company/")
    description = models.TextField(max_length=1000, default="", blank=True, null=True)

    email = models.EmailField(
        max_length=500,
        default="default@default.com",
        blank=True,
        null=True,
    )
    phone = models.CharField(max_length=150, default="01099999", blank=True)

    facebook = models.URLField(max_length=500, blank=True)
    linkedin = models.URLField(max_length=500, blank=True)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        err = "You can't delete this object"
        raise ValidationError(err)

    def clean(self, *args, **kwargs):
        if MainSettings.objects.exists() and not self.pk:
            err = "You can not create more than one object"
            raise ValidationError(err)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "MainSettings"

    # def logo_tag(self):
    #     return mark_safe(f'<img src="{self.logo.url}" width="150" height="70"/>')
