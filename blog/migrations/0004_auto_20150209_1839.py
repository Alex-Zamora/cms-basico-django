# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_imagepost'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categorías'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'Entradas del blog'},
        ),
    ]
