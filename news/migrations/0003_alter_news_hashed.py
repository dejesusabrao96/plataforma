# Generated by Django 4.2 on 2024-11-15 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_hashed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='hashed',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]
