# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20150112_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='url',
            field=models.CharField(default=datetime.datetime(2015, 2, 10, 0, 9, 26, 797765, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
