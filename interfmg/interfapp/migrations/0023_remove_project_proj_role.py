# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0022_project_proj_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='proj_role',
        ),
    ]
