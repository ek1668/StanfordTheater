# Generated by Django 3.0.5 on 2020-04-22 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stanford_theater', '0002_pictures_year'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pictures',
            new_name='Movie',
        ),
    ]