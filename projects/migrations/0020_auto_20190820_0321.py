# Generated by Django 2.2.4 on 2019-08-20 07:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_auto_20190820_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 20, 3, 21, 19, 354895), verbose_name='date published'),
        ),
    ]
