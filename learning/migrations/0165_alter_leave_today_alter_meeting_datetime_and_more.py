# Generated by Django 5.0.1 on 2024-03-19 11:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0164_oauthcredentials_user_alter_leave_today_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='today',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 19, 11, 38, 55, 801644)),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='datetime',
            field=models.DateTimeField(default=datetime.time(11, 38, 55, 820554)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='half_daytime',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 3, 19, 11, 38, 55, 782662)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='in_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 3, 19, 11, 38, 55, 782662)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='late_mark_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 3, 19, 11, 38, 55, 782662)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='out_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 3, 19, 11, 38, 55, 782662)),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateField(default=datetime.datetime(2024, 3, 19, 11, 38, 55, 781669)),
        ),
    ]