# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-20 04:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_arxivxml'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arxivxml',
            name='authors',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='arxivxml',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
