# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-24 10:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Offshores', '0007_auto_20160723_1849'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='beneficiariesoffshores',
            options={'verbose_name': 'Офшор-Бенефициар', 'verbose_name_plural': 'Офшоры-Бенефициары'},
        ),
        migrations.AlterModelOptions(
            name='offshoresassets',
            options={'verbose_name': 'Офшор-Актив', 'verbose_name_plural': 'Офшоры-Активы'},
        ),
    ]