# Generated by Django 2.2.4 on 2019-08-21 00:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0022_auto_20190820_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 20, 20, 47, 23, 619545), verbose_name='date published'),
        ),
    ]
