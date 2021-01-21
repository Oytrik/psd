# Generated by Django 3.1 on 2021-01-21 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tms', '0006_auto_20210121_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ps2tstransfer',
            name='sub_type',
            field=models.IntegerField(choices=[(0, 'PS to TS (Single Degree)'), (1, 'PS-PS to PS-TS (Dual Degree)'), (2, 'PS-PS to TS-PS (Dual Degree)'), (3, 'TS-PS to TS-TS (Dual Degree)')], null=True),
        ),
    ]
