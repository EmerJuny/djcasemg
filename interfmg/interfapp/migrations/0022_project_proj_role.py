# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0021_project_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='proj_role',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
