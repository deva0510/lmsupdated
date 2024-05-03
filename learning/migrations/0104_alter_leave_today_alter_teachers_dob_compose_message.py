# Generated by Django 5.0.1 on 2024-02-07 14:31

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0103_alter_leave_today_alter_teachers_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='today',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 7, 14, 31, 25, 991570)),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateField(default=datetime.datetime(2024, 2, 7, 14, 31, 25, 970628)),
        ),
        migrations.CreateModel(
            name='compose_message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MessageType', models.CharField(max_length=100)),
                ('Message', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('studentname', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learning.student')),
                ('teachername', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learning.teachers')),
            ],
        ),
    ]
