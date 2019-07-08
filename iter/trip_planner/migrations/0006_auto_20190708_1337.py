# Generated by Django 2.1 on 2019-07-08 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip_planner', '0005_auto_20190704_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='TripDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Trip_id', models.IntegerField(default=0)),
                ('detail_type', models.IntegerField(default=3)),
                ('detail', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='trip',
            name='Description',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='start_time',
        ),
        migrations.AddField(
            model_name='trip',
            name='days',
            field=models.IntegerField(default=0),
        ),
    ]
