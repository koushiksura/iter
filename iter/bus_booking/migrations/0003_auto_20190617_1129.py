# Generated by Django 2.2.2 on 2019-06-17 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus_booking', '0002_auto_20190614_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus_agency',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
