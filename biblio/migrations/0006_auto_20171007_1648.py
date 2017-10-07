# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0005_auto_20171007_1646'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Videos',
            new_name='Video',
        ),
        migrations.AlterField(
            model_name='book',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 6, 14, 48, 6, 329661, tzinfo=utc)),
        ),
    ]
