# Generated by Django 4.1.7 on 2023-02-23 15:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_booking_reservation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='reservation_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]