# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0038_auto_20170412_1941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interfaces',
            old_name='excuteResult',
            new_name='result',
        ),
        migrations.RemoveField(
            model_name='interfaces',
            name='dels',
        ),
        migrations.RemoveField(
            model_name='interfaces',
            name='name',
        ),
        migrations.RemoveField(
            model_name='interfaces',
            name='summary',
        ),
        migrations.AddField(
            model_name='case',
            name='interName',
            field=models.ForeignKey(default=1, to='interfapp.Interfaces'),
            preserve_default=False,
        ),
    ]
