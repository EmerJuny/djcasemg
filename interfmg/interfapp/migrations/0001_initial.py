# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('summary', models.CharField(max_length=60)),
                ('details', models.CharField(max_length=255, null=True)),
                ('createtime', models.DateField(auto_now_add=True)),
                ('lastUpdateTime', models.DateField()),
                ('dels', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Interfaces',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('interfName', models.CharField(max_length=30)),
                ('interfDns', models.CharField(max_length=30)),
                ('interfPath', models.CharField(max_length=50)),
                ('interfMethod', models.CharField(max_length=10)),
                ('interfParams', models.CharField(max_length=255)),
                ('excuteResult', models.CharField(max_length=30, null=True)),
                ('createTime', models.DateField(auto_now_add=True)),
                ('lastUpdateTime', models.DateField()),
                ('dels', models.BooleanField()),
                ('case', models.ForeignKey(to='interfapp.Case')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('um', models.CharField(max_length=30, null=True)),
                ('role', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('dels', models.BooleanField()),
                ('responsible', models.ForeignKey(to='interfapp.Owner')),
            ],
        ),
        migrations.AddField(
            model_name='interfaces',
            name='owner',
            field=models.ForeignKey(to='interfapp.Owner'),
        ),
        migrations.AddField(
            model_name='interfaces',
            name='project',
            field=models.ForeignKey(to='interfapp.Project'),
        ),
        migrations.AddField(
            model_name='case',
            name='owner',
            field=models.ForeignKey(to='interfapp.Owner'),
        ),
    ]
