# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0005_auto_20170322_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='role',
            field=models.IntegerField(default=1, choices=[(1, b'\xe6\xb5\x8b\xe8\xaf\x95'), (2, b'\xe5\xbc\x80\xe5\x8f\x91')]),
        ),
    ]
