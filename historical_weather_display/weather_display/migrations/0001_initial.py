# Generated by Django 2.1.2 on 2018-10-28 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='beijing',
            fields=[
                ('weather_date', models.DateField(primary_key=True, serialize=False)),
                ('max_temp', models.CharField(max_length=10)),
                ('min_temp', models.CharField(max_length=10)),
                ('weather', models.CharField(max_length=30)),
                ('wind_direct', models.CharField(max_length=30)),
                ('wind_speed', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'beijing',
                'managed': False,
            },
        ),
    ]
