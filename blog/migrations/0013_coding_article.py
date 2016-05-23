# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20160523_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='coding',
            name='article',
            field=models.TextField(default=1, verbose_name='文章'),
            preserve_default=False,
        ),
    ]
