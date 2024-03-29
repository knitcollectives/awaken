# Generated by Django 2.2.4 on 2019-08-11 21:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(default=datetime.datetime(2019, 8, 11, 21, 53, 46, 49745), verbose_name='date published')),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(related_name='posts', to='blog.Category')),
            ],
        ),
    ]
