# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-23 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Offshores', '0005_auto_20160723_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiariesoffshores',
            name='beneficiary',
            field=models.ForeignKey(on_delete=models.SET(''), to='Offshores.Beneficiary', verbose_name='бенефициар'),
        ),
        migrations.AlterField(
            model_name='beneficiariesoffshores',
            name='offshore',
            field=models.ForeignKey(on_delete=models.SET(''), to='Offshores.Offshore', verbose_name='офшор'),
        ),
        migrations.AlterField(
            model_name='offshoresassets',
            name='asset',
            field=models.ForeignKey(on_delete=models.SET(''), to='Offshores.Asset', verbose_name='актив'),
        ),
        migrations.AlterField(
            model_name='offshoresassets',
            name='offshore',
            field=models.ForeignKey(on_delete=models.SET(''), to='Offshores.Offshore', verbose_name='офшор'),
        ),
    ]