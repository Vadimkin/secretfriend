# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150217_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friend_id',
            field=models.ForeignKey(related_name='friend', blank=True, editable=False, to='users.User', null=True),
            preserve_default=True,
        ),
    ]
