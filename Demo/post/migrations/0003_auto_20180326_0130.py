# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-26 01:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='uid',
            field=models.IntegerField(),
        ),
    ]
