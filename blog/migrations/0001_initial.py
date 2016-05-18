# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('user', models.CharField(max_length=50, verbose_name="User's name ")),
                ('passwd', models.CharField(max_length=50, verbose_name="User's password ")),
                ('email', models.EmailField(max_length=50, verbose_name="User's email address ")),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='User cratedate ')),
            ],
        ),
    ]
