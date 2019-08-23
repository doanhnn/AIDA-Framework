# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20171201_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='panel',
            name='description',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='panel',
            name='menu_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='panel',
            name='visible',
            field=models.BooleanField(default='True'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='widget',
            name='visible',
            field=models.BooleanField(default='True'),
            preserve_default=False,
        ),
    ]