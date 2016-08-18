# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-14 12:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('Codesample', '0016_auto_20160814_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='fotos',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 14, 12, 7, 16, 94876)),
        ),
        migrations.AlterField(
            model_name='fotos',
            name='name',
            field=models.CharField(default=b'20160814_120716', max_length=20),
        ),
    ]