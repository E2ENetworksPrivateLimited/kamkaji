# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-11-21 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_manager', '0003_jobmanager_handler'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobmanager',
            name='queue_host',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='jobmanager',
            name='job_id',
            field=models.IntegerField(default=1),
        ),
    ]
