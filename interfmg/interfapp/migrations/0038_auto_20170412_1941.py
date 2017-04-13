# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0037_auto_20170412_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interfaces',
            name='summary',
            field=models.ForeignKey(to='interfapp.Case'),
        ),
    ]
