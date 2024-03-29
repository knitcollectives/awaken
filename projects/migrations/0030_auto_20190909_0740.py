# Generated by Django 2.2.4 on 2019-09-09 11:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0029_auto_20190909_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='static/img'),
        ),
        migrations.AlterField(
            model_name='project',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 9, 7, 40, 59, 178672), verbose_name='date published'),
        ),
    ]
