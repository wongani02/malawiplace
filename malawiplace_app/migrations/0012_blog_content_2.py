# Generated by Django 3.2 on 2022-05-21 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('malawiplace_app', '0011_airline_airline_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content_2',
            field=models.TextField(blank=True),
        ),
    ]