# Generated by Django 2.2.4 on 2019-08-11 22:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190811_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 11, 22, 8, 47, 147120), verbose_name='date published'),
        ),
    ]
