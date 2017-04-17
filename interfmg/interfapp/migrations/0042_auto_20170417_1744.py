# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0041_interfaces_header'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interfaces',
            name='header',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
