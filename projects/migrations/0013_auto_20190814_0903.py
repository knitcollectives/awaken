# Generated by Django 2.2.4 on 2019-08-14 13:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20190813_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 14, 9, 3, 4, 907938), verbose_name='date published'),
        ),
    ]