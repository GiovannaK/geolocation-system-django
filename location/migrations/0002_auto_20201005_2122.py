# Generated by Django 3.1.2 on 2020-10-06 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Measurement',
            new_name='Location',
        ),
    ]
