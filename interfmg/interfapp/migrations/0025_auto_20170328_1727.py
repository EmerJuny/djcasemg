# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0024_auto_20170328_1723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='owner_id',
            new_name='owner',
        ),
    ]
