# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 02:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pivot_v2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gpa',
            old_name='major_details',
            new_name='major',
        ),
    ]