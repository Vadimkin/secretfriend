# coding=utf-8
import datetime
import random


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


def site_mode():
    REGISTRATION_MODE = 0
    GAME_MODE = 1
    RESULTS_MODE = 2

    if datetime.date.today() < datetime.date(2015, 2, 8):
        return REGISTRATION_MODE
    elif datetime.date.today() < datetime.date(2015, 3, 20):
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

        one_user.friend = all_active_users.get(id=random_id)
        one_user.save()

        users_random.remove(random_id)