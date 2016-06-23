# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 19:39
from __future__ import unicode_literals

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
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(choices=[('gvl', 'Greenville'), ('avl', 'Asheville'), ('clt', 'Charlotte'), ('hou', 'Houston')], max_length=15)),
                ('listing_type', models.CharField(choices=[('fs', 'For Sale'), ('re', 'Real Estate'), ('btr', 'Barter'), ('srv', 'Service')], max_length=15)),
                ('category', models.CharField(choices=[('owner', 'By-Owner'), ('dealer', 'By-Dealer')], max_length=15)),
                ('title', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='listing_photos', verbose_name='Listing Photo')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(choices=[('gvl', 'Greenville'), ('avl', 'Asheville'), ('clt', 'Charlotte'), ('hou', 'Houston')], max_length=15)),
                ('contact', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
