# Generated by Django 2.2.4 on 2019-08-20 08:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_auto_20190820_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 20, 4, 18, 25, 795079), verbose_name='date published'),
        ),
    ]
