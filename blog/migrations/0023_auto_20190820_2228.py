# Generated by Django 2.2.4 on 2019-08-21 02:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20190820_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 20, 22, 28, 33, 447346), verbose_name='date published'),
        ),
    ]