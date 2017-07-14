# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-14 18:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0010_auto_20170714_1052'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackfillType',
            fields=[
                ('who_created', models.CharField(max_length=30)),
                ('when_created', models.DateTimeField(blank=True, null=True)),
                ('who_updated', models.CharField(max_length=30)),
                ('when_updated', models.DateTimeField(blank=True, null=True)),
                ('backfill_type_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=100)),
                ('is_hidden', models.BooleanField(default=False)),
                ('sort_order', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'gwells_backfill_type',
                'ordering': ['sort_order', 'description'],
            },
        ),
        migrations.CreateModel(
            name='SurfaceSealMaterial',
            fields=[
                ('who_created', models.CharField(max_length=30)),
                ('when_created', models.DateTimeField(blank=True, null=True)),
                ('who_updated', models.CharField(max_length=30)),
                ('when_updated', models.DateTimeField(blank=True, null=True)),
                ('surface_seal_material_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=100)),
                ('is_hidden', models.BooleanField(default=False)),
                ('sort_order', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'gwells_surface_seal_material',
                'ordering': ['sort_order', 'description'],
            },
        ),
        migrations.CreateModel(
            name='SurfaceSealMethod',
            fields=[
                ('who_created', models.CharField(max_length=30)),
                ('when_created', models.DateTimeField(blank=True, null=True)),
                ('who_updated', models.CharField(max_length=30)),
                ('when_updated', models.DateTimeField(blank=True, null=True)),
                ('surface_seal_method_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=100)),
                ('is_hidden', models.BooleanField(default=False)),
                ('sort_order', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'gwells_surface_seal_method',
                'ordering': ['sort_order', 'description'],
            },
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='backfill_depth',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Backfill Depth'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='surface_seal_depth',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Surface Seal Depth'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='surface_seal_thickness',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Surface Seal Thickness'),
        ),
        migrations.AddField(
            model_name='well',
            name='backfill_depth',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Backfill Depth'),
        ),
        migrations.AddField(
            model_name='well',
            name='surface_seal_depth',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Surface Seal Depth'),
        ),
        migrations.AddField(
            model_name='well',
            name='surface_seal_thickness',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Surface Seal Thickness'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='backfill_type',
            field=models.ForeignKey(blank=True, db_column='backfill_type_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.BackfillType', verbose_name='Backfill Type'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='surface_seal_material',
            field=models.ForeignKey(blank=True, db_column='surface_seal_material_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.SurfaceSealMaterial', verbose_name='Surface Seal Material'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='surface_seal_method',
            field=models.ForeignKey(blank=True, db_column='surface_seal_method_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.SurfaceSealMethod', verbose_name='Surface Seal Installation Method'),
        ),
        migrations.AddField(
            model_name='well',
            name='backfill_type',
            field=models.ForeignKey(blank=True, db_column='backfill_type_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.BackfillType', verbose_name='Backfill Type'),
        ),
        migrations.AddField(
            model_name='well',
            name='surface_seal_material',
            field=models.ForeignKey(blank=True, db_column='surface_seal_material_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.SurfaceSealMaterial', verbose_name='Surface Seal Material'),
        ),
        migrations.AddField(
            model_name='well',
            name='surface_seal_method',
            field=models.ForeignKey(blank=True, db_column='surface_seal_method_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.SurfaceSealMethod', verbose_name='Surface Seal Installation Method'),
        ),
    ]
