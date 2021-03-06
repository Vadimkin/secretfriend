# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20150218_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='friend',
            field=models.ForeignKey(related_name='user_id', editable=False, to='users.User', null=True),
            preserve_default=True,
        ),
    ]
