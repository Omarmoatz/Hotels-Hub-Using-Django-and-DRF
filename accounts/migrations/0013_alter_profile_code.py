# Generated by Django 5.0.3 on 2024-07-09 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_profile_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='code',
            field=models.CharField(blank=True, default='3PJqr5rFao5KAwXcA8Q0', max_length=200, null=True),
        ),
    ]