# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0029_auto_20170330_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='owner',
            field=models.ForeignKey(to='interfapp.Owner'),
        ),
        migrations.AlterField(
            model_name='case',
            name='project',
            field=models.ForeignKey(default=1, to='interfapp.Project'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.ForeignKey(to='interfapp.Owner'),
        ),
    ]
