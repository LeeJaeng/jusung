# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mileage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mileage',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='mileage',
            name='tel',
        ),
        migrations.AlterField(
            model_name='mileage',
            name='stu_name',
            field=models.CharField(max_length=2),
        ),
    ]
