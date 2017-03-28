# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0016_auto_20170324_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='createtime',
        ),
        migrations.RemoveField(
            model_name='case',
            name='lastUpdateTime',
        ),
        migrations.AlterField(
            model_name='case',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
    ]
