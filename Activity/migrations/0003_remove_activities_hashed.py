# Generated by Django 4.2 on 2024-11-05 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Activity', '0002_alter_activities_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activities',
            name='hashed',
        ),
    ]