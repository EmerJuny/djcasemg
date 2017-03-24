# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0013_project_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='project',
            field=models.ForeignKey(blank=True, to='interfapp.Project', null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
