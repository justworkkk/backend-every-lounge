# Generated by Django 5.1.2 on 2024-11-03 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='has_provided_location',
            field=models.BooleanField(default=False),
        ),
    ]
