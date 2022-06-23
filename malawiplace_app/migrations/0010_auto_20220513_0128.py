# Generated by Django 3.2 on 2022-05-12 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('malawiplace_app', '0009_about_contactdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_name', models.CharField(max_length=200, null=True)),
                ('logo', models.ImageField(upload_to='logos/')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=200, null=True)),
                ('about_place', models.TextField(null=True)),
                ('extra_content', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('company_name', models.CharField(max_length=100, null=True)),
                ('content', models.TextField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='company_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='facebook_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='instagram_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='open_days',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='open_time',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='phone_number',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='twitter_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]