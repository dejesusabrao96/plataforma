# Generated by Django 5.1.1 on 2024-10-18 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectImplementation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Data Implemetasaun')),
                ('activity', models.TextField(verbose_name='Deskridsaun Actividade')),
                ('amount_of_funds', models.CharField(max_length=300, null=True, verbose_name='Montante Orcamento')),
                ('Funder', models.CharField(max_length=300, verbose_name='Funder')),
                ('contact_person', models.CharField(max_length=300, verbose_name='Contact Person')),
            ],
            options={
                'verbose_name': 'activity',
                'verbose_name_plural': 'activities',
                'ordering': ['-date'],
            },
        ),
    ]