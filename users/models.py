# coding=utf-8
from django.db import models, connection
from users.utils import FACULTIES_TYPES, COURSE_TYPES


class User(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ім'я")
    vk_link = models.CharField(max_length=200, verbose_name="Профіль VK")
    faculty = models.IntegerField(max_length=1, choices=FACULTIES_TYPES, default=0, verbose_name="Факультет")
    course = models.IntegerField(max_length=1, choices=COURSE_TYPES, default=1, verbose_name="Курс")
    group_num = models.CharField(max_length=200, verbose_name="Номер групи")
    mobile_num = models.CharField(max_length=200, verbose_name="Номер мобільного")
    is_active = models.BooleanField(default=0, verbose_name="Чи дозволена участь у грі")
    friend = models.ForeignKey('self', related_name='user_id', editable=True, null=True, blank=True)
    hash_code = models.CharField(max_length=200, verbose_name="Secret Key", default="")

    is_friends_before_start = models.BooleanField(default=False, verbose_name="Були друзями до старту гри")
    is_friends_after_end = models.BooleanField(default=False, verbose_name="Стали друзями після кінця гри")

    def get_faculty(self):
        return FACULTIES_TYPES[self.faculty][1]

    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"

    def __unicode__(self):
        return u"{0}".format(self.name)