# Generated by Django 5.0.3 on 2024-07-12 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0008_remove_hotel_rating_alter_booking_booking_code'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
