# Generated by Django 3.0.5 on 2020-04-25 02:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stanford_theater', '0003_auto_20200421_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]