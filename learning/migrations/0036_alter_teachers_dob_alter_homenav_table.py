# Generated by Django 5.0.1 on 2024-01-11 12:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0035_alter_teachers_dob_alter_homenav_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateField(default=datetime.datetime(2024, 1, 11, 12, 2, 38, 969855)),
        ),
        migrations.AlterModelTable(
            name='homenav',
            table='learnapp_homenav',
        ),
    ]
