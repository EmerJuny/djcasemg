# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0035_auto_20170410_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='checkPoint',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
