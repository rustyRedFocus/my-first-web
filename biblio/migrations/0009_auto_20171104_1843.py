# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0008_auto_20171104_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='photo',
        ),
        migrations.AddField(
            model_name='video',
            name='photo',
            field=models.ImageField(upload_to='./static/media', default=datetime.datetime(2017, 11, 4, 17, 43, 3, 871739, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 4, 17, 42, 55, 168878, tzinfo=utc)),
        ),
    ]
