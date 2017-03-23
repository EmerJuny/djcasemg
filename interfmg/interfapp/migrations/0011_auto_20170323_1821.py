# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0010_auto_20170323_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.CharField(max_length=20),
        ),
    ]
