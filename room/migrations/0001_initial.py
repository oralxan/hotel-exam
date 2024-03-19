# Generated by Django 4.2.8 on 2024-03-15 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotel', '0002_alter_hotel_address_alter_hotel_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1, verbose_name='number')),
                ('capacity', models.IntegerField(default=1, verbose_name='capacity')),
                ('price_per_night', models.IntegerField(verbose_name='price_per_night')),
                ('is_used', models.BooleanField(default=False, verbose_name='Is used')),
                ('description', models.TextField(blank=True, null=True, verbose_name='about room')),
                ('hotel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel', verbose_name='hatel')),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
            },
        ),
    ]