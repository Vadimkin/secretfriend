# coding=utf-8
from django.contrib import admin
from django.db import connection, ProgrammingError
from users.models import User


class UserAdmin(admin.ModelAdmin):
    # fields = ['name', 'vk_link', 'faculty', 'course', 'group_num', 'mobile_num']
    list_display = ['name', 'vk_link', 'faculty', 'course', 'group_num', 'mobile_num', 'is_active', 'friend',
                    'get_history']

    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    make_active.short_description = "Дозволити участь у грі"

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)

    make_inactive.short_description = "Заборонити участь у грі"

    def remove_friend(self, request, queryset):
        queryset.update(friend=None)

    remove_friend.short_description = "Видалити друга"

    actions = [make_active, make_inactive]

    def get_history(self, instance):
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT `user`.`name`, `user`.`is_send_gift`, `user`.`is_get_gift`, `from_friend`.`is_send_gift` as `get_gift`, `to_friend`.`is_get_gift`\
                            FROM `sfznu` user\
                            JOIN `sfznu` from_friend ON from_friend.friend_id = user.id\
                            JOIN `sfznu` to_friend ON user.friend_id = to_friend.id WHERE `user`.`mobile` =  %s;",
                           [instance.mobile_num])

            row = cursor.fetchone()
            if row:
                result = ""
                result += "<strong style='color: green;'>Отправлял подарок</strong>" if row[
                                                                                            1] == 1 else "Не отправлял подарок"
                result += " [получатель получил подарок]" if row[4] == 1 else " [получатель не получил подарок]"
                result += "<br>"
                result += "Получила подарок" if row[2] == 1 else "Не получила подарок"
                result += " [ТД отправлял подарок]" if row[3] == 1 else " [ТД не отправлял подарок]"
                result += "<br><small>{0}</small>".format(row[0].encode('utf-8'))
                return result
            else:
                return "Нет данных"
        except ProgrammingError:
            return "Не создана таблица"

    get_history.allow_tags = True


admin.site.register(User, UserAdmin)