# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0006_owner_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='role',
            field=models.CharField(max_length=4),
        ),
    ]
