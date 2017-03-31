# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0030_auto_20170331_1646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='owner',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='case',
            old_name='project',
            new_name='projectName',
        ),
    ]
