# Generated by Django 5.0.1 on 2024-02-07 14:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0099_remove_teacher_shifts_facult_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='today',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 7, 14, 29, 25, 106065)),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateField(default=datetime.datetime(2024, 2, 7, 14, 29, 25, 84140)),
        ),
    ]
