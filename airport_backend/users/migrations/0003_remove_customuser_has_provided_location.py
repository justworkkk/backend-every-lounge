# Generated by Django 5.1.2 on 2024-11-03 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_has_provided_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='has_provided_location',
        ),
    ]
