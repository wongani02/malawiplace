# Generated by Django 3.2 on 2022-05-07 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('malawiplace_app', '0004_auto_20220507_0323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('img', models.ImageField(blank=True, upload_to='blog_img')),
                ('category', models.CharField(choices=[('Travel', 'Travel'), ('Cars', 'Cars'), ('Nature', 'Nature')], max_length=200, null=True)),
            ],
        ),
    ]
