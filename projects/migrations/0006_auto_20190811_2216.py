# Generated by Django 2.2.4 on 2019-08-11 22:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20190811_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 11, 22, 16, 33, 701812), verbose_name='date published'),
        ),
    ]
