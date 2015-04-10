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
    (2, None),
    (3, u'іноземної філології'),
    (4, u'фізичного виховання'),
    (5, u'історичний'),
    (6, u'математичний'),
    (7, u'юридичний'),
    (8, u'менеджменту'),
    (9, u'філологічний'),
    (10, u'фізичний'),
    (11, u'соціальної педагогіки та психології'),
    (12, u'соцiологiї та управлiння'),
    (13, u'економічний'),
    (14, u'ЕПК')
)

COURSE_TYPES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
)


def site_mode():
    REGISTRATION_MODE = 0
    GAME_MODE = 1
    RESULTS_MODE = 2

    if datetime.date.today() < datetime.date(2015, 4, 1):
        return REGISTRATION_MODE
    elif datetime.date.today() < datetime.date(2015, 4, 10):
        return GAME_MODE
    else:
        return RESULTS_MODE


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
    from secretfriend.settings_local import VK_TOKEN

    all_active_users = User.objects.filter(is_active=1)

    data = {
        'user_ids': ",".join([user.vk_link for user in all_active_users]),
        'fields': 'screen_name',
        'access_token': VK_TOKEN
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