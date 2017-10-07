# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0004_auto_20171007_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=4)),
                ('status', models.CharField(choices=[('b', 'Borrowed'), ('a', 'Available')], max_length=2, default='a')),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 6, 14, 46, 28, 497879, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('b', 'Borrowed'), ('a', 'Available')], max_length=2, default='a'),
        ),
    ]
