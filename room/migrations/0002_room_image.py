# Generated by Django 4.2.8 on 2024-03-18 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='image',
            field=models.ImageField(default=1, upload_to='rooms-img/%Y/%m/%d', verbose_name='image of room'),
            preserve_default=False,
        ),
    ]
