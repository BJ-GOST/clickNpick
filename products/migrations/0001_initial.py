# Generated by Django 4.1.5 on 2023-04-17 18:36

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('category', models.CharField(max_length=255, null=True)),
                ('units', models.CharField(max_length=255, null=True)),
                ('price', models.IntegerField(null=True)),
                ('description', models.TextField(null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('seller', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='agency', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='Image')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.product')),
            ],
        ),
    ]