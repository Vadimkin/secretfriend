# coding=utf-8
from django.db import models
from users.utils import FACULTIES_TYPES, COURSE_TYPES


class User(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ім'я")
    vk_link = models.CharField(max_length=200, verbose_name="Профіль VK")
    faculty = models.IntegerField(max_length=1, choices=FACULTIES_TYPES, default=0, verbose_name="Факультет")
    course = models.IntegerField(max_length=1, choices=COURSE_TYPES, default=1, verbose_name="Курс")
    group_num = models.CharField(max_length=200, verbose_name="Номер групи")
    mobile_num = models.CharField(max_length=200, verbose_name="Номер мобільного")
    is_active = models.BooleanField(default=0, verbose_name="Чи дозволена участь у грі")

    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"

    def __unicode__(self):
        return u"{0}".format(self.name)