# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-02 14:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tax', '0003_teacher_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='Course',
            new_name='course',
        ),
    ]
