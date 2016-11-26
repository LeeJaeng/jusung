# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mileage', '0002_auto_20161126_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='mileage',
            name='gender',
            field=models.CharField(null=True, max_length=2),
        ),
        migrations.AddField(
            model_name='mileage',
            name='tel',
            field=models.CharField(null=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='mileage',
            name='stu_name',
            field=models.CharField(null=True, max_length=16),
        ),
    ]
