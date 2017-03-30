# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0026_auto_20170328_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='ownerId',
            field=models.ForeignKey(related_name='ownerId', on_delete=django.db.models.deletion.PROTECT, verbose_name='name', to='interfapp.Owner'),
        ),
    ]
