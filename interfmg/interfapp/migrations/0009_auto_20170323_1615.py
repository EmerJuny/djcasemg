# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0008_auto_20170322_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.CharField(max_length=20),
        ),
    ]
