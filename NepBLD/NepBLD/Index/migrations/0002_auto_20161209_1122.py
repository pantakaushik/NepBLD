# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-09 11:22
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerclass',
            name='name_slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='first_name', unique_with=['first_name', 'last_name']),
        ),
    ]
