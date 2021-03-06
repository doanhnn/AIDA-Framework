# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-02 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_widget_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='widget',
            name='data',
        ),
        migrations.AlterField(
            model_name='panel',
            name='description',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='panel',
            name='visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='widget',
            name='description',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='widget',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
