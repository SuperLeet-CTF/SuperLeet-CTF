# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 11:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('challenges', '__first__'),
        ('questionnaire', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=256)),
                ('score', models.IntegerField(default=0, editable=False)),
                ('attempted_quizzes', models.ManyToManyField(blank=True, to='questionnaire.Quiz')),
                ('solved_challenges', models.ManyToManyField(blank=True, to='challenges.Challenge')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
