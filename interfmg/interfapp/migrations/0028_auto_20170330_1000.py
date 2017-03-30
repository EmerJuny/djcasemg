# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0027_auto_20170330_0954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='ownerId',
        ),
        migrations.AlterField(
            model_name='project',
            name='ownerName',
            field=models.ForeignKey(related_name='ownerName', on_delete=django.db.models.deletion.PROTECT, verbose_name='name', to='interfapp.Owner'),
        ),
    ]
