# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160520_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coding',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('img', models.ImageField(blank=True, upload_to='img', null=True)),
                ('createTime', models.DateTimeField(auto_now=True)),
                ('article', models.TextField(verbose_name='文章')),
                ('tag', models.CharField(max_length=10, verbose_name='标签')),
                ('title', models.CharField(max_length=20, verbose_name='标题')),
                ('view_count', models.IntegerField(verbose_name='浏览次数', default=0)),
                ('praise_count', models.IntegerField(verbose_name='点赞次数', default=0)),
                ('author', models.ForeignKey(to='blog.User')),
            ],
        ),
    ]
