# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-03-31 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('emailid', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('reviews', models.TextField()),
            ],
        ),
    ]
