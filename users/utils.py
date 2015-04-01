# coding=utf-8
import datetime
import random


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
    elif datetime.date.today() < datetime.date(2015, 4, 22):
        # generate_friends()
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