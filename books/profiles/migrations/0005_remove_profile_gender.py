# Generated by Django 3.1.1 on 2021-02-28 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
    ]
