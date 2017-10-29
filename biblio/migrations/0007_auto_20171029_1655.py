# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0006_auto_20171007_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='description',
            field=models.TextField(default=datetime.datetime(2017, 10, 29, 15, 55, 53, 874399, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 28, 15, 55, 47, 202732, tzinfo=utc)),
        ),
    ]
