# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('imageIndex', models.ImageField(upload_to='blog/')),
                ('slug', models.SlugField(max_length=255, blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='blog.Category')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='user',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
