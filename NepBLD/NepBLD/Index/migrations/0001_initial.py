# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-09 11:16
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('middle_name', models.CharField(max_length=100, verbose_name='Middle Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='last Name')),
                ('name_slug', autoslug.fields.AutoSlugField(editable=False, populate_from=['first_name', 'last_name'])),
            ],
        ),
    ]
