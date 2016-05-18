# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160512_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feeling',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('img', models.ImageField(upload_to='blog/static/img')),
                ('feeling', models.CharField(max_length=200, verbose_name='说说 ')),
                ('createTime', models.DateTimeField(auto_now=True)),
                ('like_times', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Say',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('saying', models.CharField(max_length=50, verbose_name='Saying everday ')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='feeling',
            name='person',
            field=models.ForeignKey(to='blog.User'),
        ),
    ]
