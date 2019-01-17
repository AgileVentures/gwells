# Generated by Django 2.1.4 on 2019-01-08 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0046_auto_20181213_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitysubmission',
            name='observation_well_number',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name='Observation Well Number'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='observation_well_status',
            field=models.ForeignKey(blank=True, db_column='obs_well_status_code', null=True, on_delete=django.db.models.deletion.PROTECT, to='wells.ObsWellStatusCode', verbose_name='Observation Well Status'),
        ),
        migrations.AlterField(
            model_name='well',
            name='observation_well_status',
            field=models.ForeignKey(blank=True, db_column='obs_well_status_code', null=True, on_delete=django.db.models.deletion.PROTECT, to='wells.ObsWellStatusCode', verbose_name='Observation Well Status'),
        ),
    ]