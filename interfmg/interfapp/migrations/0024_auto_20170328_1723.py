# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0023_remove_project_proj_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='owner',
            new_name='owner_id',
        ),
        migrations.AddField(
            model_name='project',
            name='ownerName',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
