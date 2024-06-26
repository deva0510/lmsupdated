# Generated by Django 5.0.1 on 2024-03-26 17:39

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0178_alter_leave_today_alter_teacher_shifts_half_daytime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='today',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 26, 17, 39, 19, 743069)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='half_daytime',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 3, 26, 17, 39, 19, 713420)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='in_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 3, 26, 17, 39, 19, 713420)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='late_mark_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 3, 26, 17, 39, 19, 713420)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='out_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 3, 26, 17, 39, 19, 713420)),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateField(default=datetime.datetime(2024, 3, 26, 17, 39, 19, 713420)),
        ),
        migrations.CreateModel(
            name='fee_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms', models.CharField(default='', max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('first_name', models.CharField(default='', max_length=255)),
                ('s_class', models.CharField(default='', max_length=255)),
                ('term1', models.CharField(default='', max_length=100)),
                ('term2', models.CharField(default='', max_length=100)),
                ('term3', models.CharField(default='', max_length=100)),
                ('amountpaid', models.CharField(default='', max_length=100)),
                ('schoolid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learning.schools')),
                ('student_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learning.student')),
            ],
        ),
    ]
