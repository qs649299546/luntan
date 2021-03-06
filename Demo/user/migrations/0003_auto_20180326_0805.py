# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-26 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_perm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
                ('level', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='perm',
        ),
        migrations.AddField(
            model_name='user',
            name='perm_id',
            field=models.IntegerField(default=1),
        ),
    ]
