# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0004_auto_20170320_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='dels',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='role',
        ),
        migrations.RemoveField(
            model_name='project',
            name='dels',
        ),
    ]
