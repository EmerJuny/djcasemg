# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0002_auto_20170316_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='summary',
            field=models.CharField(max_length=100),
        ),
    ]
