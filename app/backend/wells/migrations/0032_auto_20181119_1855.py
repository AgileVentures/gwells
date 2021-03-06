# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-19 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0031_auto_20181119_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='well',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Town/City'),
        ),
        migrations.AlterField(
            model_name='well',
            name='consultant_company',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Consultant Company'),
        ),
        migrations.AlterField(
            model_name='well',
            name='development_notes',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Development Notes'),
        ),
        migrations.AlterField(
            model_name='well',
            name='driller_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Name of Person Who Did the Work'),
        ),
        migrations.AlterField(
            model_name='well',
            name='legal_block',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Block'),
        ),
        migrations.AlterField(
            model_name='well',
            name='legal_district_lot',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='District Lot'),
        ),
        migrations.AlterField(
            model_name='well',
            name='legal_lot',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Lot'),
        ),
        migrations.AlterField(
            model_name='well',
            name='legal_plan',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Plan'),
        ),
        migrations.AlterField(
            model_name='well',
            name='legal_range',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Range'),
        ),
        migrations.AlterField(
            model_name='well',
            name='legal_section',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='well',
            name='legal_township',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Township'),
        ),
        migrations.AlterField(
            model_name='well',
            name='other_screen_bottom',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Specify Other Screen Bottom'),
        ),
        migrations.AlterField(
            model_name='well',
            name='other_screen_material',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Specify Other Screen Material'),
        ),
        migrations.AlterField(
            model_name='well',
            name='owner_postal_code',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Postal Code'),
        ),
        migrations.AlterField(
            model_name='well',
            name='street_address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Street Address'),
        ),
        migrations.AlterField(
            model_name='well',
            name='water_quality_colour',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Water Quality Colour'),
        ),
        migrations.AlterField(
            model_name='well',
            name='water_quality_odour',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Water Quality Odour'),
        ),
        migrations.AlterField(
            model_name='well',
            name='well_location_description',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Description of Well Location'),
        ),
    ]
