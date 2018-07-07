# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 11:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trashcan', '0004_auto_20160927_0610'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='harvest',
            unique_together=set([('user', 'trash_can', 'date')]),
        ),
    ]
