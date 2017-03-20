# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfapp', '0003_auto_20170317_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='dels',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='case',
            name='details',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='interfaces',
            name='dels',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='interfaces',
            name='interfParams',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='owner',
            name='role',
            field=models.CharField(max_length=1, choices=[(b'T', b'\xe6\xb5\x8b\xe8\xaf\x95'), (b'D', b'\xe5\xbc\x80\xe5\x8f\x91')]),
        ),
        migrations.AlterField(
            model_name='project',
            name='dels',
            field=models.BooleanField(default=False),
        ),
    ]
