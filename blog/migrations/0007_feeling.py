# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160518_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feeling',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('img', models.ImageField(upload_to='img')),
                ('feeling', models.CharField(max_length=200, verbose_name='说说 ')),
                ('createTime', models.DateTimeField(auto_now=True)),
                ('like_times', models.IntegerField(default=0)),
                ('person', models.ForeignKey(to='blog.User')),
            ],
        ),
    ]
