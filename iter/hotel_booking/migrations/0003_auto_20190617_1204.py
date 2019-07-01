# Generated by Django 2.2.2 on 2019-06-17 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_booking', '0002_auto_20190614_1125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rooms',
            old_name='discount',
            new_name='price',
        ),
        migrations.AddField(
            model_name='rooms',
            name='room_fac',
            field=models.IntegerField(default=1),
        ),
    ]
