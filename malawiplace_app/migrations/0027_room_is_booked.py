# Generated by Django 4.0.5 on 2022-06-22 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('malawiplace_app', '0026_bookevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='is_booked',
            field=models.BooleanField(default=False),
        ),
    ]
