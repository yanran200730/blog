# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_coding_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coding',
            name='tag',
            field=models.CharField(max_length=20, verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='coding',
            name='title',
            field=models.CharField(max_length=50, verbose_name='标题'),
        ),
    ]
