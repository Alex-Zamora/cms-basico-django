# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20141117_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagePost',
            field=models.ImageField(upload_to='blog/', blank=True, default=datetime.datetime(2015, 1, 13, 17, 31, 48, 158149, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
