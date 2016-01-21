# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20160121_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ip_user',
            field=models.GenericIPAddressField(default=b'127.0.0.1', verbose_name=b'IP'),
        ),
        migrations.AlterField(
            model_name='user',
            name='university',
            field=models.IntegerField(choices=[(0, '\u0417\u041d\u0423'), (1, '\u041a\u041f\u0423')], default=0, verbose_name=b'\xd0\xa3\xd0\xbd\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x80\xd1\x81\xd0\xb8\xd1\x82\xd0\xb5\xd1\x82'),
        ),
    ]