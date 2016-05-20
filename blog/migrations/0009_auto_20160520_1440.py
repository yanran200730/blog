# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=20, verbose_name='标题', default='2016/5/20 14:40'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.CharField(max_length=10, verbose_name='标签'),
        ),
    ]
