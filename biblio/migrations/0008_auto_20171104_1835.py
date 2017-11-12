# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0007_auto_20171029_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='photo',
            field=models.ImageField(upload_to='blabla', default=datetime.datetime(2017, 11, 4, 17, 35, 55, 714621, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 4, 17, 35, 38, 71429, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('b', 'Borrowed'), ('a', 'Available')], max_length=9, default='a'),
        ),
        migrations.AlterField(
            model_name='video',
            name='status',
            field=models.CharField(choices=[('borrowed', 'Borrowed'), ('available', 'Available')], max_length=9, default='available'),
        ),
    ]
