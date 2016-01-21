# coding=utf-8
import datetime
import json
import random
import string
from time import sleep
import urllib
import urllib2

from django.db.models import Q

FACULTIES_TYPES = (
    (0, u'журналістики'),
    (1, u'біологічний'),
    (2, u'іноземної філології'),
    (3, u'фізичного виховання'),
    (4, u'історичний'),
    (5, u'математичний'),
    (6, u'юридичний'),
    (7, u'менеджменту'),
    (8, u'філологічний'),
    (9, u'фізичний'),
    (10, u'соціальної педагогіки та психології'),
    (11, u'соцiологiї та управлiння'),
    (12, u'економічний'),
    (13, u'ЕПК'),

    (14, u'Інститут права ім. Володимира Сташиса'),
    (15, u'Інститут іноземної філології'),
    (16, u'Інститут економіки'),
    (17, u'Інститут управління'),
    (18, u'Інститут здоров\'я, спорту і туризму'),
    (19, u'Інститут журналістики і масових комунікацій'),
    (20, u'Коледж КПУ')
)

COURSE_TYPES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
)

UNIVERSITY_TYPES = (
    (0, u'ЗНУ'),
    (1, u'КПУ')
)


def site_mode():
    registration_mode = 0
    game_mode = 1
    results_mode = 2

    if datetime.date.today() <= datetime.date(2016, 2, 13):  # February, 2
        return registration_mode
    elif datetime.date.today() < datetime.date(2016, 2, 20):
        return game_mode
    else:
        return results_mode


def generate_friends():
    from users.models import User

    all_active_users = User.objects.filter(is_active=1)
    users_random = [user.id for user in all_active_users]

    for one_user in all_active_users:
        random_id = None
        while random_id is None or random_id == one_user.id:
            random_id = random.choice(users_random)
            if all_active_users.get(id=random_id).id == one_user.id:
                random_id = None

        one_user.hash_code = one_user.mobile_num[5:10]

        one_user.friend = all_active_users.get(id=random_id)
        one_user.save()

        users_random.remove(random_id)


def update_hash():
    from users.models import User

    all_active_users = User.objects.filter(is_active=1)

    for one_user in all_active_users:
        one_user.hash_code = ''.join(random.choice(string.digits) for _ in range(7))
        one_user.save()


def check_is_friends():
    from users.models import User

    all_active_users = User.objects.filter(is_active=1)

    data = {
        'user_ids': ",".join([user.vk_link for user in all_active_users]),
        'fields': 'screen_name'
    }

    request = urllib2.Request(url="https://api.vk.com/method/users.get?" + urllib.urlencode(data))
    result = json.loads(urllib2.urlopen(request).read())

    for vk_user in result['response']:
        try:
            user = User.objects.filter(
                    Q(vk_link='id' + str(vk_user['uid'])) | Q(vk_link=vk_user[u'screen_name']) | Q(
                            vk_link=str(vk_user['uid'])))
        except KeyError:
            continue

        user.update(vk_link=vk_user['uid'])

    for user in all_active_users:
        try:
            request = urllib2.Request(
                    url="https://api.vk.com/method/friends.get?" + urllib.urlencode({'user_id': user.vk_link}))
            result = json.loads(urllib2.urlopen(request).read())

            if int(user.friend.vk_link) in result['response']:
                user.is_friends_before_start = True
                user.save()
        except (KeyError, ValueError):
            continue

        print(user)

        sleep(0.5)
