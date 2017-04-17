# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0040_auto_20170413_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='interfaces',
            name='header',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
