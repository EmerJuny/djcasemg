# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0032_auto_20170331_1802'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interfaces',
            old_name='case',
            new_name='summary',
        ),
    ]
