# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-16 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Offshores', '0002_auto_20160816_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offshore',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
