# Generated by Django 5.0.1 on 2024-02-22 11:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0137_alter_adminphoto_image_alter_applogo_logo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff_prob',
            name='p1',
        ),
        migrations.AddField(
            model_name='staff_imp',
            name='image2',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='staff_imp',
            name='main_heading1',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='staff_prob',
            name='image',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='today',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 22, 11, 35, 52, 985127)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='half_daytime',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 2, 22, 11, 35, 52, 959233)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='in_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 2, 22, 11, 35, 52, 959233)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='late_mark_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 2, 22, 11, 35, 52, 959233)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='out_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 2, 22, 11, 35, 52, 959233)),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateField(default=datetime.datetime(2024, 2, 22, 11, 35, 52, 958235)),
        ),
    ]