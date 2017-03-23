# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0012_remove_project_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
