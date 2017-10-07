# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('BR', 'Borrowed'), ('AV', 'Available')], default='BR', max_length=2),
        ),
        migrations.AlterField(
            model_name='book',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 6, 13, 45, 12, 787243, tzinfo=utc)),
        ),
    ]
