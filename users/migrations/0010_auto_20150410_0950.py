# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20150401_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_friends_after_end',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\xa1\xd1\x82\xd0\xb0\xd0\xbb\xd0\xb8 \xd0\xb4\xd1\x80\xd1\x83\xd0\xb7\xd1\x8f\xd0\xbc\xd0\xb8 \xd0\xbf\xd1\x96\xd1\x81\xd0\xbb\xd1\x8f \xd0\xba\xd1\x96\xd0\xbd\xd1\x86\xd1\x8f \xd0\xb3\xd1\x80\xd0\xb8'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='is_friends_before_start',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x91\xd1\x83\xd0\xbb\xd0\xb8 \xd0\xb4\xd1\x80\xd1\x83\xd0\xb7\xd1\x8f\xd0\xbc\xd0\xb8 \xd0\xb4\xd0\xbe \xd1\x81\xd1\x82\xd0\xb0\xd1\x80\xd1\x82\xd1\x83 \xd0\xb3\xd1\x80\xd0\xb8'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='faculty',
            field=models.IntegerField(default=0, max_length=1, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xba\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb5\xd1\x82', choices=[(0, '\u0436\u0443\u0440\u043d\u0430\u043b\u0456\u0441\u0442\u0438\u043a\u0438'), (1, '\u0431\u0456\u043e\u043b\u043e\u0433\u0456\u0447\u043d\u0438\u0439'), (2, None), (3, '\u0456\u043d\u043e\u0437\u0435\u043c\u043d\u043e\u0457 \u0444\u0456\u043b\u043e\u043b\u043e\u0433\u0456\u0457'), (4, '\u0444\u0456\u0437\u0438\u0447\u043d\u043e\u0433\u043e \u0432\u0438\u0445\u043e\u0432\u0430\u043d\u043d\u044f'), (5, '\u0456\u0441\u0442\u043e\u0440\u0438\u0447\u043d\u0438\u0439'), (6, '\u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u0447\u043d\u0438\u0439'), (7, '\u044e\u0440\u0438\u0434\u0438\u0447\u043d\u0438\u0439'), (8, '\u043c\u0435\u043d\u0435\u0434\u0436\u043c\u0435\u043d\u0442\u0443'), (9, '\u0444\u0456\u043b\u043e\u043b\u043e\u0433\u0456\u0447\u043d\u0438\u0439'), (10, '\u0444\u0456\u0437\u0438\u0447\u043d\u0438\u0439'), (11, '\u0441\u043e\u0446\u0456\u0430\u043b\u044c\u043d\u043e\u0457 \u043f\u0435\u0434\u0430\u0433\u043e\u0433\u0456\u043a\u0438 \u0442\u0430 \u043f\u0441\u0438\u0445\u043e\u043b\u043e\u0433\u0456\u0457'), (12, '\u0441\u043e\u0446i\u043e\u043b\u043e\u0433i\u0457 \u0442\u0430 \u0443\u043f\u0440\u0430\u0432\u043bi\u043d\u043d\u044f'), (13, '\u0435\u043a\u043e\u043d\u043e\u043c\u0456\u0447\u043d\u0438\u0439'), (14, '\u0415\u041f\u041a')]),
            preserve_default=True,
        ),
    ]
