# Generated by Django 4.0.5 on 2022-06-15 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('malawiplace_app', '0024_buscompany_bus_bookbus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookbus',
            options={'verbose_name_plural': 'Book Buses'},
        ),
        migrations.AlterModelOptions(
            name='buscompany',
            options={'verbose_name_plural': 'Bus Companies'},
        ),
        migrations.AddField(
            model_name='bookbus',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
