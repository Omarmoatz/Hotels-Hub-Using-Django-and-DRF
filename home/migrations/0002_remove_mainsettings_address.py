# Generated by Django 5.0.4 on 2024-05-09 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainsettings',
            name='address',
        ),
    ]
