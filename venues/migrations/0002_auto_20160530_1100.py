# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-30 09:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursevenue',
            options={'ordering': ['updated_date']},
        ),
    ]