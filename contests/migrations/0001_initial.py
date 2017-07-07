# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-07 12:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('creators', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
