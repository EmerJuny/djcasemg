# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0033_auto_20170401_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interfaces',
            name='excuteResult',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
