# coding=utf-8
from django.db import models
from users.utils import FACULTIES_TYPES, COURSE_TYPES


class User(models.Model):
    name = models.CharField(max_length=200)
    vk_link = models.CharField(max_length=200)
    facult = models.IntegerField(max_length=1, choices=FACULTIES_TYPES, default=0)
    course = models.IntegerField(max_length=1, choices=COURSE_TYPES, default=1)
    group_num = models.CharField(max_length=200)
    mobile_num = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Друг"
        verbose_name_plural = "Друга"