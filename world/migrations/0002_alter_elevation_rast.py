# Generated by Django 4.2.4 on 2023-08-24 16:02

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elevation',
            name='rast',
            field=django.contrib.gis.db.models.fields.RasterField(max_length=100, srid=4326),
        ),
    ]