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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('vk_link', models.CharField(max_length=200)),
                ('faculty', models.IntegerField(default=0, max_length=1, choices=[(0, b'\xd0\xb6\xd1\x83\xd1\x80\xd0\xbd\xd0\xb0\xd0\xbb\xd1\x96\xd1\x81\xd1\x82\xd0\xb8\xd0\xba\xd0\xb8'), (1, b'\xd0\xb1\xd1\x96\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb3\xd1\x96\xd1\x87\xd0\xbd\xd0\xb8\xd0\xb9'), (3, b'\xd1\x96\xd0\xbd\xd0\xbe\xd0\xb7\xd0\xb5\xd0\xbc\xd0\xbd\xd0\xbe\xd1\x97 \xd1\x84\xd1\x96\xd0\xbb\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb3\xd1\x96\xd1\x97'), (4, b'\xd1\x84\xd1\x96\xd0\xb7\xd0\xb8\xd1\x87\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xb2\xd0\xb8\xd1\x85\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8f'), (5, b'\xd1\x96\xd1\x81\xd1\x82\xd0\xbe\xd1\x80\xd0\xb8\xd1\x87\xd0\xbd\xd0\xb8\xd0\xb9'), (6, b'\xd0\xbc\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbc\xd0\xb0\xd1\x82\xd0\xb8\xd1\x87\xd0\xbd\xd0\xb8\xd0\xb9'), (7, b'\xd1\x8e\xd1\x80\xd0\xb8\xd0\xb4\xd0\xb8\xd1\x87\xd0\xbd\xd0\xb8\xd0\xb9'), (8, b'\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xb4\xd0\xb6\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd1\x83'), (9, b'\xd1\x84\xd1\x96\xd0\xbb\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb3\xd1\x96\xd1\x87\xd0\xbd\xd0\xb8\xd0\xb9'), (10, b'\xd1\x84\xd1\x96\xd0\xb7\xd0\xb8\xd1\x87\xd0\xbd\xd0\xb8\xd0\xb9'), (11, b'\xd1\x81\xd0\xbe\xd1\x86\xd1\x96\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xbe\xd1\x97 \xd0\xbf\xd0\xb5\xd0\xb4\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xb3\xd1\x96\xd0\xba\xd0\xb8 \xd1\x82\xd0\xb0 \xd0\xbf\xd1\x81\xd0\xb8\xd1\x85\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb3\xd1\x96\xd1\x97'), (12, b'\xd1\x81\xd0\xbe\xd1\x86i\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb3i\xd1\x97 \xd1\x82\xd0\xb0 \xd1\x83\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbbi\xd0\xbd\xd0\xbd\xd1\x8f')])),
                ('course', models.IntegerField(default=1, max_length=1, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('group_num', models.CharField(max_length=200)),
                ('mobile_num', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': '\u0414\u0440\u0443\u0433',
                'verbose_name_plural': '\u0414\u0440\u0443\u0433\u0430',
            },
            bases=(models.Model,),
        ),
    ]