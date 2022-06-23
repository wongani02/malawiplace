# Generated by Django 3.2 on 2022-05-06 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline_name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarRental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=100)),
                ('room_category', models.CharField(choices=[('Deluxe', 'Deluxe'), ('Standard', 'Standard'), ('Executive', 'Executive'), ('Presidential', 'Presidential')], max_length=400)),
                ('check_in', models.DateField(blank=True, null=True)),
                ('check_out', models.DateField(blank=True, null=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='malawiplace_app.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_name', models.CharField(max_length=200, null=True)),
                ('Final_destination', models.CharField(max_length=200, null=True)),
                ('depature_place', models.CharField(max_length=200, null=True)),
                ('depature_date', models.DateField(blank=True, null=True)),
                ('return_ticket', models.BooleanField(default=False)),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='malawiplace_app.airline')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_type', models.CharField(choices=[('', ''), ('', ''), ('', '')], max_length=100, null=True)),
                ('car_name', models.CharField(max_length=200, null=True)),
                ('pick_up', models.DateTimeField(blank=True, null=True)),
                ('Drop_off', models.DateTimeField(blank=True, null=True)),
                ('passengers', models.IntegerField(default=1)),
                ('car_rental', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='malawiplace_app.carrental')),
            ],
        ),
    ]
