# Generated by Django 2.2.4 on 2019-09-07 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20190901_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 7, 8, 26, 23, 253925), verbose_name='date published'),
        ),
    ]
