# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0036_case_checkpoint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interfaces',
            name='summary',
            field=models.ForeignKey(related_name='CIN', to='interfapp.Case'),
        ),
    ]
