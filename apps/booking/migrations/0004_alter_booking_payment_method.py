# Generated by Django 5.0.9 on 2024-10-27 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('processing', 'Processing'), ('paid', 'Paid'), ('failed', 'Failed')], max_length=10),
        ),
    ]