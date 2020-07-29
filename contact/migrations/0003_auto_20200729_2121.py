# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-29 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20200729_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(default='', max_length=1024),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]