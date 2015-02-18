# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_friend_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='friend_id',
        ),
        migrations.AddField(
            model_name='user',
            name='friend',
            field=models.ForeignKey(related_name='friend_id', blank=True, editable=False, to='users.User', null=True),
            preserve_default=True,
        ),
    ]
