# Generated by Django 3.0.5 on 2020-04-25 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stanford_theater', '0005_movie_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
