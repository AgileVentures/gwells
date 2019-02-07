# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-21 16:56
from __future__ import unicode_literals

from django.db import migrations
import json
from io import open
import os
from gwells.codes import CodeFixture


def code_fixture():
    fixture = '0038_lithology_moisture_codes.json'
    fixture_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), fixture)

    return CodeFixture(fixture_path)


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0037_merge_20181204_1950'),
    ]

    operations = [
        migrations.RunPython(code_fixture().load_fixture, reverse_code=code_fixture().unload_fixture),
    ]