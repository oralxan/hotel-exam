# Generated by Django 4.2.8 on 2024-03-19 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_rename_author_booking_guest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='guest',
            new_name='author',
        ),
    ]