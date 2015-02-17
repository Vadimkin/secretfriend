# coding=utf-8
from django.db import models


class User(models.Model):
    FACULTIES_TYPES = (
        (0, 'журналістики'),
        (1, 'біологічний'),
        (3, 'іноземної філології'),
        (4, 'фізичного виховання'),
        (5, 'історичний'),
        (6, 'математичний'),
        (7, 'юридичний'),
        (8, 'менеджменту'),
        (9, 'філологічний'),
        (10, 'фізичний'),
        (11, 'соціальної педагогіки та психології'),
        (12, 'соцiологiї та управлiння')
    )

    COURSE_TYPES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )

    name = models.CharField(max_length=200)
    vk_link = models.CharField(max_length=200)
    facult = models.IntegerField(max_length=1, choices=FACULTIES_TYPES, default=0)
    course = models.IntegerField(max_length=1, choices=COURSE_TYPES, default=1)
    group_num = models.CharField(max_length=200)
    mobile_num = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Друг"
        verbose_name_plural = "Друга"