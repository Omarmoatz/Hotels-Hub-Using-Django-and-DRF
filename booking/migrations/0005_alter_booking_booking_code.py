# Generated by Django 5.0.3 on 2024-07-24 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_coupon_alter_booking_booking_code_alter_booking_room_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_code',
            field=models.CharField(blank=True, default='2hLzMuuLmF', max_length=500, null=True),
        ),
    ]