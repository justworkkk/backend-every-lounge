# Generated by Django 5.1.2 on 2024-11-04 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lounge',
            old_name='airport',
            new_name='airport_id',
        ),
    ]