# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0019_auto_20170328_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='owner',
        ),
    ]
