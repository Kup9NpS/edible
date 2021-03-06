# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-08 16:25
from __future__ import unicode_literals

import carts.models
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
            name='Carts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_color', models.CharField(choices=[('Red', 'Red'), ('Green', 'Green')], default='Red', max_length=5)),
                ('title', models.CharField(max_length=120)),
                ('img', models.ImageField(blank=True, height_field='img_height', upload_to='', verbose_name='Изображение товара', width_field='img_width')),
                ('img_height', models.PositiveIntegerField(default=200)),
                ('img_width', models.PositiveIntegerField(default=200)),
                ('place', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('is_public', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='carts',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.Category'),
        ),
        migrations.AddField(
            model_name='carts',
            name='user',
            field=models.ForeignKey(on_delete=models.SET(carts.models.get_deleted_user), to=settings.AUTH_USER_MODEL),
        ),
    ]
