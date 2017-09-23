# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='created_date',
            new_name='borrow_date',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='text',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='published_date',
            new_name='return_date',
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=200),
        ),
    ]
