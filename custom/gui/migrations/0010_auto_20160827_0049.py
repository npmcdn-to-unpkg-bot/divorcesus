# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-27 04:49
from __future__ import unicode_literals

from django.db import migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0009_auto_20160827_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=redactor.fields.RedactorField(verbose_name='Answer'),
        ),
    ]