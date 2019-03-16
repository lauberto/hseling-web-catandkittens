# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-25 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollocationFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collocations', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='MetaFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='WordFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('words', models.FileField(upload_to='')),
            ],
        ),
    ]