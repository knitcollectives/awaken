# Generated by Django 2.2.4 on 2019-11-19 05:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_auto_20191119_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 19, 0, 18, 1, 895431), verbose_name='date published'),
        ),
    ]
