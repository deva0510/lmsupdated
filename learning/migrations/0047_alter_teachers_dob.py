# Generated by Django 5.0.1 on 2024-01-22 16:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0046_alter_teachers_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 22, 16, 58, 54, 366389)),
        ),
    ]