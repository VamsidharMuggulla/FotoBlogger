# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-16 11:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Codesample', '0025_auto_20160816_0903'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fotos',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 16, 11, 3, 11, 194598)),
        ),
        migrations.AlterField(
            model_name='fotos',
            name='name',
            field=models.CharField(default=b'20160816_110311', max_length=20),
        ),
    ]
