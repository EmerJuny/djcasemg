# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0015_auto_20170324_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='owner',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='case',
            name='project',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
    ]
