# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-16 11:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Codesample', '0026_auto_20160816_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotos',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 16, 11, 11, 6, 770862)),
        ),
        migrations.AlterField(
            model_name='fotos',
            name='name',
            field=models.CharField(default=b'20160816_111106', max_length=20),
        ),
    ]