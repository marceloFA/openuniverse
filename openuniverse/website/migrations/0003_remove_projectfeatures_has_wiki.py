# Generated by Django 2.1.2 on 2018-11-05 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_timeseries_data_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectfeatures',
            name='has_wiki',
        ),
    ]
