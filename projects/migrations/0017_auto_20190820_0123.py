# Generated by Django 2.2.4 on 2019-08-20 05:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_auto_20190819_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 20, 1, 23, 7, 304788), verbose_name='date published'),
        ),
    ]
