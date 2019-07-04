# Generated by Django 2.2.2 on 2019-07-03 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bus_booking', '0008_auto_20190619_1211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bus',
            old_name='journeydate',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='reach_time',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='reachdate',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='bus_booking',
            name='agency_id',
        ),
        migrations.RemoveField(
            model_name='bus_booking',
            name='journeydate',
        ),
        migrations.RemoveField(
            model_name='bus_booking',
            name='journeytime',
        ),
        migrations.RemoveField(
            model_name='bus_booking',
            name='noofseats',
        ),
        migrations.RemoveField(
            model_name='bus_booking',
            name='reachdate',
        ),
        migrations.RemoveField(
            model_name='bus_booking',
            name='reachtime',
        ),
        migrations.RemoveField(
            model_name='via',
            name='reach_date',
        ),
        migrations.RemoveField(
            model_name='via',
            name='reach_time',
        ),
        migrations.RemoveField(
            model_name='via',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='via',
            name='start_time',
        ),
        migrations.AddField(
            model_name='bus',
            name='distance_from_startcity',
            field=models.FloatField(default=600),
        ),
        migrations.AddField(
            model_name='bus',
            name='reach',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bus',
            name='start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bus_booking',
            name='Bus_model',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='bus_booking',
            name='bus_start_date',
            field=models.DateField(default='2019-06-29'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bus_booking',
            name='destination_city',
            field=models.CharField(default='hyderabad', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bus_booking',
            name='reach',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bus_booking',
            name='start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bus_booking',
            name='start_city',
            field=models.CharField(default='tirupati', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='via',
            name='reach',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bus',
            name='Bus_model',
            field=models.CharField(choices=[('scania', 'scania'), ('volvo', 'volvo'), ('super luxary', 'super luxary'), ('Normal', 'Normal')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='bus',
            name='Bus_type',
            field=models.CharField(choices=[('Sleeper', 'Sleeper'), ('Semi Sleeper', 'Semi Sleeper'), ('Seater', 'Seater')], max_length=20),
        ),
        migrations.AlterField(
            model_name='bus',
            name='noseats',
            field=models.IntegerField(default=40),
        ),
        migrations.AlterField(
            model_name='bus',
            name='seats_available',
            field=models.CharField(default='????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????', max_length=1000),
        ),
        migrations.AlterField(
            model_name='bus_booking',
            name='bus_type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='bus_booking',
            name='serviceno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus_booking.Bus'),
        ),
        migrations.CreateModel(
            name='bus_dates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus_booking.Bus')),
            ],
        ),
    ]
