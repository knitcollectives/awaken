# Generated by Django 2.2.4 on 2019-08-20 05:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20190820_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 20, 1, 28, 43, 236942), verbose_name='date published'),
        ),
    ]
