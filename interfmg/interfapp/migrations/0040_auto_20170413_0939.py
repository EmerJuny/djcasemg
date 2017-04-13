# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0039_auto_20170413_0907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='interName',
            new_name='interfName',
        ),
    ]
