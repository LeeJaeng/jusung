# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mileage',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('stu_name', models.TextField()),
                ('tel', models.TextField()),
                ('birth', models.DateField(null=True, blank=True)),
                ('gender', models.BooleanField()),
                ('mileage', models.IntegerField()),
                ('saving_date', models.DateTimeField(null=True, blank=True)),
                ('using_date', models.DateTimeField(null=True, blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
