# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-03 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Offshores', '0015_auto_20160803_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetsbeneficiaries',
            name='rel_date',
            field=models.DateField(blank=True, null=True, verbose_name='дата актуальности'),
        ),
    ]
