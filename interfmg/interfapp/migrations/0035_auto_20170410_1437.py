# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0034_auto_20170405_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interfaces',
            name='interfDns',
            field=models.CharField(max_length=255),
        ),
    ]
