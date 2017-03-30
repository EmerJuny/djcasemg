# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0028_auto_20170330_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='ownerName',
        ),
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=1, to='interfapp.Owner'),
            preserve_default=False,
        ),
    ]
