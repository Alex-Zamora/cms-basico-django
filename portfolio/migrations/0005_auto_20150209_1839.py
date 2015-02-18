# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20150209_1814'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolio',
            options={'verbose_name_plural': 'portafolio'},
        ),
        migrations.AlterModelOptions(
            name='technology',
            options={'verbose_name_plural': 'tecnologías web'},
        ),
    ]
