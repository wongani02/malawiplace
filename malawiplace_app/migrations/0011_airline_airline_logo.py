# Generated by Django 3.2 on 2022-05-21 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('malawiplace_app', '0010_auto_20220513_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='airline',
            name='airline_logo',
            field=models.ImageField(blank=True, upload_to='airline_logo/'),
        ),
    ]