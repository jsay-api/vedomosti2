# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-03 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Offshores', '0010_offshore_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offshore',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='offshores/'),
        ),
    ]