# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0014_auto_20170324_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='lastUpdateTime',
            field=models.DateField(auto_now_add=True),
        ),
    ]
