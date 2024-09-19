from django.db import models
from django.utils.html import mark_safe
from model_utils.models import TimeStampedModel


class MainSettings(TimeStampedModel):
    name = models.CharField( max_length=150)
    logo = models.ImageField( upload_to='company/')
    description = models.TextField( max_length=1000, default='', blank=True, null=True)

    email = models.EmailField( max_length=500, default='default@default.com', blank=True, null=True)
    phone = models.CharField( max_length=150, default='01099999', blank=True, null=True)

    facebook = models.URLField( max_length=500, blank=True, null=True)
    linkedin = models.URLField( max_length=500, blank=True, null=True)

    def delete(self, *args, **kwargs):
        raise Exception("You can't delete this object")
    
    def save(self,*args, **kwargs):
        if MainSettings.objects.exists() and not self.pk:
            raise Exception('You can not create more than one object')
        return super(MainSettings, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'MainSettings'

    # def logo_tag(self):
    #     return mark_safe(f'<img src="{self.logo.url}" width="150" height="70"/>')