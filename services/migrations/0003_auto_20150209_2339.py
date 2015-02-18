# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20150209_1839'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name_plural': 'Servicios'},
        ),
    ]
