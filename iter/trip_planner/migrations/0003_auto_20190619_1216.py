# Generated by Django 2.1 on 2019-06-19 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip_planner', '0002_distances'),
    ]

    operations = [
        migrations.AddField(
            model_name='distances',
            name='distance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='distances',
            name='time',
            field=models.FloatField(default=0),
        ),
    ]