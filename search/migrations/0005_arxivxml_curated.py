# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-20 22:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20170820_0432'),
    ]

    operations = [
        migrations.AddField(
            model_name='arxivxml',
            name='curated',
            field=models.BooleanField(default=False),
        ),
    ]