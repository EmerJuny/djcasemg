# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0031_auto_20170331_1729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interfaces',
            old_name='owner',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='interfaces',
            old_name='project',
            new_name='projectName',
        ),
        migrations.AlterField(
            model_name='interfaces',
            name='createTime',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='interfaces',
            name='interfMethod',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='interfaces',
            name='lastUpdateTime',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
