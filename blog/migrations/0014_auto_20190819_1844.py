# Generated by Django 2.2.4 on 2019-08-19 22:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20190818_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 19, 18, 44, 55, 488939), verbose_name='date published'),
        ),
    ]
