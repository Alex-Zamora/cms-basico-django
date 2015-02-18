# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_portfolio_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='url',
            field=models.CharField(blank=True, max_length=100),
            preserve_default=True,
        ),
    ]
