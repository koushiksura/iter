# Generated by Django 2.2.2 on 2019-06-19 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus_booking', '0007_auto_20190619_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus_booking',
            name='id',
        ),
        migrations.RemoveField(
            model_name='bus_booking',
            name='seatno',
        ),
        migrations.AddField(
            model_name='bus_booking',
            name='noofseats',
            field=models.CharField(default=1, max_length=5),
        ),
        migrations.AddField(
            model_name='passenger',
            name='seatno',
            field=models.CharField(default=1, max_length=5),
        ),
        migrations.AlterField(
            model_name='bus_booking',
            name='booking_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('others', 'others')], max_length=6),
        ),
    ]
