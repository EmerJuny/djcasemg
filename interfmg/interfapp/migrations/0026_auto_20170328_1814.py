# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0025_auto_20170328_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='owner',
        ),
        migrations.AddField(
            model_name='project',
            name='ownerId',
            field=models.ForeignKey(related_name='ownerId', on_delete=django.db.models.deletion.PROTECT, default=1, to='interfapp.Owner'),
            preserve_default=False,
        ),
    ]
