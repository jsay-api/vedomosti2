# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-16 20:11
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Offshores', '0003_auto_20160816_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='offshore',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]