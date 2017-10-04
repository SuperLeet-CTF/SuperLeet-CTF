# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 11:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contests', '0001_initial'),
        ('tags', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=256)),
                ('slug', models.SlugField(max_length=16, unique=True)),
                ('hints', models.CharField(blank=True, max_length=256)),
                ('score', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=25, unique=True)),
                ('description', models.CharField(blank=True, max_length=256)),
                ('score', models.IntegerField(default=0, editable=False)),
                ('difficulty', models.CharField(choices=[('n00b', 'n00b'), ('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard'), ('1337', '1337')], max_length=10)),
                ('hidden', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('contest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contests.Contest')),
                ('creators', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='tags.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='MCQ',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='questionnaire.Question')),
                ('choices', models.CharField(max_length=256)),
                ('answer', models.IntegerField()),
                ('is_mcq', models.BooleanField(default=True, editable=False)),
            ],
            bases=('questionnaire.question',),
        ),
        migrations.CreateModel(
            name='SimpleQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='questionnaire.Question')),
                ('answer', models.CharField(max_length=64)),
                ('is_mcq', models.BooleanField(default=False, editable=False)),
            ],
            bases=('questionnaire.question',),
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.Quiz'),
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='tags.Tag'),
        ),
    ]
