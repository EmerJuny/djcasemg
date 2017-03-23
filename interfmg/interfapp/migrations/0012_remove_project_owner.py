# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0011_auto_20170323_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='owner',
        ),
    ]
