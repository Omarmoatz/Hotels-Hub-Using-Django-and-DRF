# Generated by Django 5.0.9 on 2024-11-27 07:37

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_alter_hotel_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.IntegerField(blank=True, help_text='Rate should be between 0 and 5', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='hotel.roomtype'),
        ),
    ]