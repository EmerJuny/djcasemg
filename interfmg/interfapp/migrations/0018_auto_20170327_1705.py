# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0017_auto_20170327_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='createTime',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='case',
            name='lastUpdateTime',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
