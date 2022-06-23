# Generated by Django 4.0.5 on 2022-06-14 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('malawiplace_app', '0019_delete_bookroom_hotel_slug_alter_hotel_hotel_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255, null=True)),
                ('check_in', models.DateField(blank=True, null=True)),
                ('check_out', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_number', models.CharField(default='+265', max_length=255, null=True)),
                ('additional_reservations', models.TextField(blank=True)),
                ('number_of_rooms', models.IntegerField(default=1)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='malawiplace_app.room')),
            ],
        ),
    ]
