# Generated by Django 4.2.8 on 2024-03-19 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_rename_guest_booking_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='author',
            new_name='guest',
        ),
    ]