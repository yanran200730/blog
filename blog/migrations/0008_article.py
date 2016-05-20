# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_feeling'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('img', models.ImageField(upload_to='img')),
                ('createTime', models.DateTimeField(auto_now=True)),
                ('article', models.TextField(verbose_name='文章')),
                ('tag', models.CharField(verbose_name='标签', max_length=20)),
                ('view_count', models.IntegerField(default=0, verbose_name='浏览次数')),
                ('praise_count', models.IntegerField(default=0, verbose_name='点赞次数')),
                ('author', models.ForeignKey(to='blog.User')),
            ],
        ),
    ]
